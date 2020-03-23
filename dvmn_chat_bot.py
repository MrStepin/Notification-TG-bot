import os
from dotenv import load_dotenv
import requests
import datetime
import time
import telegram 
import logging

load_dotenv()
token = os.environ["TOKEN"]
telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]
DVMN_API = "https://dvmn.org/api/long_polling/"
headers = {"Authorization": token}
api_request_params = {"timestamp":int(time.time())}

class MyLogsHandler(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)
        bot = telegram.Bot(token=telegram_bot_token) 
        bot.send_message(chat_id=chat_id, text=log_entry)

while True:
    try:
        response = requests.get(DVMN_API, params=api_request_params, headers=headers, timeout=100)
        response.raise_for_status()
        response_status = response.json()
        if response_status['status'] == 'timeout':
            api_request_params = {"timestamp":response_status['timestamp_to_request']}
        else:
            lesson = response_status['new_attempts'][0]
            lesson_name = lesson['lesson_title']
            lesson_url = lesson['lesson_url']
            message = (f"Преподаватель проверил работу: \n {lesson_name} \n Ссылка на задачу: https://dvmn.org{lesson_url}")
            bot = telegram.Bot(token=telegram_bot_token)    
            bot.send_message(chat_id=chat_id, text=message)
            api_request_params = {"timestamp":response_status['last_attempt_timestamp']}   	
    except Exception:
        logger = logging.getLogger("Logger")
        logger.addHandler(MyLogsHandler())
        logger.exception(logger)
        