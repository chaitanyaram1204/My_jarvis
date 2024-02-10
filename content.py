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
    t1 = response.json()
    print(t1)
msg = "How is ms dhoni"
getcontent(msg)
