import os
from dotenv import load_dotenv
import requests
import datetime
import time
import telegram 

load_dotenv()
TOKEN = os.getenv("token")
TELEGRAMBOTTOKEN = os.getenv("telegramBotToken")
CHAT_ID = os.getenv("chat_id")
LIST_OF_CHECKED_TASKS = "https://dvmn.org/api/long_polling/?timestamp={}"
headers = {"Authorization": TOKEN}
timestamp = {"timestamp":int(time.time())}

while True:
    try:
        response = requests.get(LIST_OF_CHECKED_TASKS, params=timestamp, headers=headers, timeout=100)
        response.raise_for_status()
        response_status = response.json()
        if response_status['status'] == 'timeout':
            timestamp = int(response_status[timestamp_to_request])
        else:
            message = ("Преподаватель проверил работу:" + "\n" + response_status['new_attempts'][0]['lesson_title']
            + "\n" + "Ссылка на задачу: " + "https://dvmn.org" + response_status['new_attempts'][0]['lesson_url'])
            bot = telegram.Bot(token=TELEGRAMBOTTOKEN)    
            bot.send_message(chat_id=CHAT_ID, text=message)  
            break  	
    except requests.exceptions.ReadTimeout:
        print("There are no answer from the server at this moment. Waiting a response, please wait.")
        pass
    except requests.exceptions.ConnectionError:    
        print("There are no answer from the server at this moment due to internet connection problem.")
        pass

