import requests


def welcome_user():
    print("Welcome to our service!")
    # StartPoint = input("Please enter your Starting point: ")
    StartPoint = '49.89459, 10.88587'
    # EndPoint = input("Please enter your End point: ")
    EndPoint = '49.87682, 10.78936'
    ApiKey = '70H7XIcB7JygXLskc7LvDmVzjlSVi_TIBBSD_qSOQeU'
    distance, duration = get_itinerary(StartPoint, EndPoint, ApiKey)
    if distance is not None and duration is not None:
        print("Distance:", distance, "km")
        print("Duration:", duration, "minutes")
    else:
        print("No route found.")


def get_itinerary(start_point, end_point, api_key):
    url = "https://router.hereapi.com/v8/routes"
    params = {
        "transportMode": "car",
        "origin": start_point,
        "destination": end_point,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    if 'routes' in data and len(data['routes']) > 0:
        route = data['routes'][0]
        summary = route['sections'][0]['summary']
        distance = summary['length'] / 1000  # in kilometers
        duration = summary['duration'] / 60  # in minutes
        return distance, duration
    else:
        return None, None


if __name__ == "__main__":
    welcome_user()
