import os
from dotenv import load_dotenv
import requests
import datetime
import time
import telegram 
import logging

class MyLogsHandler(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)
        bot.send_message(chat_id=chat_id, text=log_entry)

logger = logging.getLogger("Logger")

        
if __name__ == '__main__':         

    load_dotenv()
    devman_token = os.environ["DEVMAN_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    DVMN_API = "https://dvmn.org/api/long_polling/"
    headers = {"Authorization": devman_token}
    api_request_params = {"timestamp":int(time.time())}
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]

    bot = telegram.Bot(token=telegram_bot_token) 
    logger.addHandler(MyLogsHandler())

    while True:
        try:
            try:
                time.sleep(2)
                response = requests.get(DVMN_API, params=api_request_params, headers=headers, timeout=100)
                response.raise_for_status()
                devman_server_response = response.json()
                if devman_server_response['status'] == 'timeout':
                    api_request_params = {"timestamp": devman_server_response['timestamp_to_request']}
            except requests.exceptions.ReadTimeout:
                pass        
            else:
                lesson = devman_server_response['new_attempts'][0]
                lesson_name = lesson['lesson_title']
                lesson_url = lesson['lesson_url']
                message = f"Преподаватель проверил работу: \n {lesson_name} \n Ссылка на задачу: https://dvmn.org{lesson_url}"   
                bot.send_message(chat_id=chat_id, text=message)
                api_request_params = {"timestamp":devman_server_response['last_attempt_timestamp']}    
        except Exception:
            logger.exception(logger)

                



