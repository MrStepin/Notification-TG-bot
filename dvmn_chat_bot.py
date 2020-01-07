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
DVMN_API = "https://dvmn.org/api/long_polling/"
headers = {"Authorization": token}
api_request_params = {"timestamp":int(time.time())}

while True:
    try:
        response = requests.get(DVMN_API, params=api_request_params, headers=headers, timeout=100)
        response.raise_for_status()
        response_status = response.json()
        if response_status['status'] == 'timeout':
            time.sleep(5)
            api_request_params = {"timestamp":response_status['timestamp_to_request']}
        else:
            lesson = response_status['new_attempts'][0]
            lesson_name = lesson['lesson_title']
            lesson_url = lesson['lesson_url']
            message = (f"Преподаватель проверил работу: \n {lesson_name} \n Ссылка на задачу: https://dvmn.org{lesson_url}")
            bot = telegram.Bot(token=telegram_bot_token)    
            bot.send_message(chat_id=chat_id, text=message)
            time.sleep(5)
            api_request_params = {"timestamp":response_status['last_attempt_timestamp']}   	
    except requests.exceptions.ReadTimeout:
        print("There are no answer from the server at this moment. Waiting a response, please wait.")
        pass
    except requests.exceptions.ConnectionError:    
        print("There are no answer from the server at this moment due to internet connection problem.")
        pass

