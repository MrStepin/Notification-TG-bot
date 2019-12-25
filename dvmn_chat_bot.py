import os
from dotenv import load_dotenv
import requests
import datetime
import time
import telegram 

load_dotenv()
token = os.getenv("TOKEN")
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
LIST_OF_CHECKED_TASKS = "https://dvmn.org/api/long_polling/"
headers = {"Authorization": token}
current_time = {"timestamp":int(time.time())}

while True:
    try:
        response = requests.get(LIST_OF_CHECKED_TASKS, params=current_time, headers=headers, timeout=100)
        response.raise_for_status()
        response_status = response.json()
        if response_status['status'] == 'timeout':
            time.sleep(5)
            current_time = {"timestamp":int(time.time())}
        else:
            attributes_of_lesson = response_status['new_attempts'][0]
            name_of_lesson = attributes_of_lesson['lesson_title']
            lesson_url = attributes_of_lesson['lesson_url']
            message = (f"Преподаватель проверил работу: \n {name_of_lesson} \n Ссылка на задачу: https://dvmn.org{lesson_url}")
            bot = telegram.Bot(token=telegram_bot_token)    
            bot.send_message(chat_id=chat_id, text=message)
            time.sleep(5)
            current_time = {"timestamp":int(time.time())}   	
    except requests.exceptions.ReadTimeout:
        print("There are no answer from the server at this moment. Waiting a response, please wait.")
        pass
    except requests.exceptions.ConnectionError:    
        print("There are no answer from the server at this moment due to internet connection problem.")
        pass

