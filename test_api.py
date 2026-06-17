"""
API Testing & Demo Script
Tests all endpoints to verify the application is working correctly
Run: python test_api.py
"""

import requests
import json
import sys
from datetime import datetime
import time

# Configuration
API_URL = "http://localhost:5000"
TIMEOUT = 5

def print_header(text):
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)

def print_success(text):
    print(f"✓ {text}")

def print_error(text):
    print(f"✗ {text}")

def print_info(text):
    print(f"ℹ {text}")

def test_health():
    """Test API health endpoint"""
    print_header("TEST 1: Health Check")
    
    try:
        response = requests.get(f"{API_URL}/health", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print_success("API is healthy")
            print(f"  Status: {data.get('status')}")
            print(f"  Models Loaded: {data.get('models_loaded')}")
            print(f"  Timestamp: {data.get('timestamp')}")
            return True
        else:
            print_error(f"Unexpected status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to API. Is Flask app running?")
        print_info(f"  Expected URL: {API_URL}")
        print_info("  Run: python app.py")
        return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_zones():
    """Test zones endpoint"""
    print_header("TEST 2: Get Zones")
    
    try:
        response = requests.get(f"{API_URL}/zones", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            zones = data.get('zones', [])
            print_success(f"Retrieved {len(zones)} zones")
            for zone in zones:
                print(f"  - {zone['zone']}: {zone['station']}")
            return True
        else:
            print_error(f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_zone_analytics():
    """Test zone analytics endpoint"""
    print_header("TEST 3: Zone Analytics")
    
    try:
        response = requests.get(f"{API_URL}/analytics/zones", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print_success(f"Retrieved analytics for {len(data)} zones")
            for zone, stats in list(data.items())[:3]:
                print(f"  - {zone}:")
                print(f"    Violations: {stats.get('violations'):,}")
                print(f"    High Severity: {stats.get('high_severity')}%")
            return True
        else:
            print_error(f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_severity_prediction():
    """Test severity prediction endpoint"""
    print_header("TEST 4: Severity Prediction")
    
    # Test data
    test_cases = [
        {
            'name': 'High-Risk Location (Peak Hour)',
            'data': {
                'latitude': 13.05,
                'longitude': 77.60,
                'cell_violations': 25,
                'cell_density': 0.95,
                'hour': 18,
                'day_of_week': 4,
                'is_peak_hour': 1,
                'has_wrong_parking': 1,
                'has_no_parking': 1,
                'has_main_road': 1
            }
        },
        {
            'name': 'Low-Risk Location (Off-Peak)',
            'data': {
                'latitude': 13.25,
                'longitude': 77.55,
                'cell_violations': 5,
                'cell_density': 0.3,
                'hour': 2,
                'day_of_week': 0,
                'is_peak_hour': 0,
                'has_wrong_parking': 0,
                'has_no_parking': 0,
                'has_main_road': 0
            }
        },
        {
            'name': 'Medium-Risk Location',
            'data': {
                'latitude': 13.15,
                'longitude': 77.65,
                'cell_violations': 15,
                'cell_density': 0.6,
                'hour': 10,
                'day_of_week': 2,
                'is_peak_hour': 0,
                'has_wrong_parking': 1,
                'has_no_parking': 0,
                'has_main_road': 1
            }
        }
    ]
    
    success_count = 0
    
    for test_case in test_cases:
        print(f"\n  Testing: {test_case['name']}")
        
        try:
            response = requests.post(
                f"{API_URL}/predict/severity",
                json=test_case['data'],
                timeout=TIMEOUT
            )
            
            if response.status_code == 200:
                result = response.json()
                print_success(f"Prediction successful")
                print(f"    Severity Score: {result.get('severity_score'):.2f}")
                print(f"    Severity Level: {result.get('severity_level')}")
                print(f"    Zone: {result.get('zone')}")
                print(f"    Station: {result.get('station')}")
                success_count += 1
            else:
                print_error(f"Status code: {response.status_code}")
        except Exception as e:
            print_error(f"Error: {str(e)}")
    
    return success_count == len(test_cases)

def test_risk_prediction():
    """Test risk prediction endpoint"""
    print_header("TEST 5: Risk Prediction")
    
    test_input = {
        'latitude': 13.05,
        'longitude': 77.60,
        'cell_violations': 20,
        'cell_density': 0.8,
        'hour': 18,
        'day_of_week': 4,
        'is_peak_hour': 1,
        'has_wrong_parking': 1,
        'has_no_parking': 0,
        'has_main_road': 1
    }
    
    try:
        response = requests.post(
            f"{API_URL}/predict/risk",
            json=test_input,
            timeout=TIMEOUT
        )
        
        if response.status_code == 200:
            result = response.json()
            print_success("Risk prediction successful")
            print(f"  Is High Risk: {result.get('is_high_risk')}")
            print(f"  Risk Probability: {result.get('risk_probability')*100:.1f}%")
            print(f"  Low Risk Probability: {result.get('low_risk_probability')*100:.1f}%")
            print(f"  Recommendation: {result.get('recommendation')}")
            return True
        else:
            print_error(f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_batch_prediction():
    """Test batch prediction endpoint"""
    print_header("TEST 6: Batch Prediction")
    
    batch_data = {
        'locations': [
            {
                'latitude': 13.05,
                'longitude': 77.60,
                'cell_violations': 20,
                'cell_density': 0.8,
                'hour': 18,
                'day_of_week': 4,
                'is_peak_hour': 1,
                'has_wrong_parking': 1,
                'has_no_parking': 0,
                'has_main_road': 1
            },
            {
                'latitude': 13.15,
                'longitude': 77.65,
                'cell_violations': 10,
                'cell_density': 0.5,
                'hour': 10,
                'day_of_week': 2,
                'is_peak_hour': 0,
                'has_wrong_parking': 0,
                'has_no_parking': 0,
                'has_main_road': 1
            },
            {
                'latitude': 13.25,
                'longitude': 77.55,
                'cell_violations': 5,
                'cell_density': 0.3,
                'hour': 2,
                'day_of_week': 0,
                'is_peak_hour': 0,
                'has_wrong_parking': 0,
                'has_no_parking': 0,
                'has_main_road': 0
            }
        ]
    }
    
    try:
        response = requests.post(
            f"{API_URL}/predict/batch",
            json=batch_data,
            timeout=TIMEOUT
        )
        
        if response.status_code == 200:
            result = response.json()
            print_success(f"Batch prediction successful")
            print(f"  Total Locations: {result.get('total_locations')}")
            predictions = result.get('predictions', [])
            print(f"  Predictions Generated: {len(predictions)}")
            for i, pred in enumerate(predictions):
                loc = pred.get('location', {})
                print(f"    Location {i+1}: ({loc.get('lat'):.2f}, {loc.get('lon'):.2f})")
                print(f"      Severity: {pred.get('severity_score'):.2f}")
                print(f"      High Risk: {pred.get('is_high_risk')}")
            return True
        else:
            print_error(f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*10 + "🚗 PARKING CONGESTION API - TEST SUITE" + " "*20 + "║")
    print("╚" + "="*68 + "╝")
    
    print(f"\nAPI URL: {API_URL}")
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tests = [
        ("Health Check", test_health),
        ("Get Zones", test_zones),
        ("Zone Analytics", test_zone_analytics),
        ("Severity Prediction", test_severity_prediction),
        ("Risk Prediction", test_risk_prediction),
        ("Batch Prediction", test_batch_prediction)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_error(f"Test failed with error: {str(e)}")
            results.append((test_name, False))
        
        time.sleep(0.5)  # Small delay between tests
    
    # Print summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nTotal Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%\n")
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {test_name}")
    
    if passed == total:
        print_success("\n🎉 ALL TESTS PASSED! Application is ready to use.")
        return True
    else:
        print_error(f"\n❌ {total - passed} test(s) failed. Check the errors above.")
        return False

if __name__ == "__main__":
    try:
        success = run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n👋 Test interrupted by user")
        sys.exit(1)
