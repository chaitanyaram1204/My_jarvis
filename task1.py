import requests

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":city,"format":"json","u":"f"}

    headers = {
        "X-RapidAPI-Key": "6df66e6f06msh5f697bd21eaf46bp1db5edjsnf8c8eefe107d",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1 = response.json()
    d1 = d1.get("current_observation")   
    hum = d1.get("atmosphere").get("humidity")
    temp = d1.get("condition").get("temperature")
    temp = round((temp-32)*5/9,2)
    return f"Temperature in {city} is {temp}°C and humidity is {hum}%"

if __name__ == "__main__":
    print(temp_city("delhi"))