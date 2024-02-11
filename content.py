from config import key
import requests #web 
from mic_to_text import mic_to_text_class
def getcontent(chat):
    data = {
        "contents" : [
            {
                "role" : "user",
                "parts" : [
                    {
                        "text" : "You are an AI bot,your name is My jarvis find the content related to query:" + " " + chat
                    }
                ]
            }
        ]
    }
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url,json = data)
    reply_api = response.json()
    
    reply = reply_api.get("candidates")[0].get("content").get("parts")[0].get("text")
    return reply
if __name__ == "__main__": 
    msg = mic_to_text_class()
    #msg = input("Enter your question :")
    getcontent(msg)
