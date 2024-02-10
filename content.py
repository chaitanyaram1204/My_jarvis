from config import key
import requests #web 

def getcontent(chat):
    data = {
        "contents" : [
            {
                "role" : "user",
                "parts" : [
                    {
                        "text" : "You are an AI bot,your name is My jarvis" + " " + chat
                    }
                ]
            }
        ]
    }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url,json = data)
    reply_api = response.json()
    
    reply = reply_api.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(reply)
msg = input("Enter your question :")
getcontent(msg)
