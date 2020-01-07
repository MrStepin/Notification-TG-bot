Notification telegram bot
=====================
 
This script send notification about checked tasks on dvmn.org

## Requirements
Python3 should be installed.  
Use pip to install dependencies:  
```pip install -r requirements.txt```

## Environment variables: 
* Create file  ```.env``` with you dvmn.org token, telegram bot token, chat id.  
Like this: ```token="Token 8e64"  
              telegram_bot_token="90303613:AA353458O4"  
              chat_id="315552"```  
## Run              
* Execute this script in CMD.
For example:  
```python dvmn_chat_bot.py```

Notification will be send to you in telegram if task will be checked.
