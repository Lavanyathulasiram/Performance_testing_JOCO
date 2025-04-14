from datetime import datetime

def build_rest_payload(date):
    return {
        "journeyList": [{
            "travelDate": date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "origin": "HYD",
            "destination": "MAA",
            "originAirportCityQualifier": "A",
            "destinationAirportCityQualifier": "A"
        }],
        "bookingType": "SEAMEN",
        "journeyType": "ONE_WAY",
        "cabinClass": "ECONOMY",
        "adultCount": 1,
        "childCount": 0,
        "infantCount": 0,
        "dateType": "DEPARTURE",
        "nationality": "India"
    }

def build_ws_payload(key, rest_payload, jwt_token, x_auth_token):
    return {
        "key": key,
        "timezone": "Asia/Kolkata",
        "accountId": 5,
        "userId": 24,
        "jwtAuthToken": jwt_token,
        "x-auth-token": x_auth_token,
        "searchParam": rest_payload
    }
