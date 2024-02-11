#this find executes the respective function based on the query
from config import key
import requests #web
import task1
from audio import text_audio


def parse_function_response(message):
    function_call = message[0].get("functionCall")
    function_name = function_call.get("name")
    """ parameters = function_call.get("parameters")
    if function_name == "temp_city":
        city = parameters.get("city")
        return task1.temp_city(city)
    elif function_name == "temp_room":
        room = parameters.get("room")
        return task1.temp_room(room)
    else:
        return "Function not found" """
    print("Gemini : call function ",function_name)

    try :
        arguments = function_call.get("args")
        print("Gemini : arguments are ",arguments)
        if arguments :
            d = getattr(task1,function_name)
            print("function is : ",d)
            function_response = d(**arguments)
    except Exception as e:
        print(e)
        function_response = "Error : Function not found"
    return function_response
def run_conversion(user_input):
    data = {
        "contents" : [
            {
                "role" : "user",
                "parts" : [
                    {
                        "text" : "You are an AI bot that can do everything using function call.When you are asked to do something, use the function call available and then respond with message" + "\n" + user_input
                    }
                ]
            }
        ],
        "tools":
        [
            {
                "functionDeclarations": task1.definitions
            }
        ]
    }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url,json = data)

    if response.status_code != 200:
        print(response.text)    
    
    reply_api = response.json()
    if "content" not in reply_api.get("candidates")[0]:
        print("Error : No content in response")
        #return "No content found"
    message = reply_api.get("candidates")[0].get("content").get("parts")
    print("Message :#############" ,message)

    if "functionCall" in message[0]:
        resp1 = parse_function_response(message)
        text_audio(resp1)
        return resp1
    else:
        return "Error : Function not found"
    """   reply = reply_api.get("candidates")[0].get("content").get("parts")[0].get("text") """
    print(reply_api)

if __name__ == "__main__":
    print(run_conversion("what is the temperature of my room"))
