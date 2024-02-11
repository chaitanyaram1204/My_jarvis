import requests
import socket

def get_ip(host):
    try:
        ip = socket.getaddrinfo("google.com",None)
        return ip
    except:
        return "Error : Host not found"

def temp_room(room):
    result = "Temperatiure in " + room + " is 25°C"
    return result
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
definitions =[
        {
            "name" : "temp_city",
            "description" : "This function takes a city name as input and returns the temperature and humidity of the city in celsius and percentage respectively.",
            "parameters" :
                {"type": "object",
                "properties":
                            {"city": 
                                {"type": "string",
                                "description": "Name of the city for which temperature and humidity is to be found."
                                }
                            }
                },
        },
        {
            "name" : "temp_room",
            "description" : "Find the temperature of my room or my home.",
            "parameters" :
                {"type": "object",
                "properties":
                            {"room": 
                                {"type": "string",
                                "description": "room or home"
                                }
                            }
                },
        },{
            "name" : "get_ip",
            "description" : "Gfind ip address of given url or domain name.",
            "parameters" :
                {"type": "object",
                "properties":
                            {"host": 
                                {"type": "string",
                                "description": "get url or domain name."
                                }
                            }
                },
        }
]
if __name__ == "__main__":
    print(temp_city("vijayawada"))