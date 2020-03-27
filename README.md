Notification telegram bot
=====================
 
This script send notification about checked tasks on dvmn.org

## Requirements
Python3 should be installed.  
Use pip to install dependencies:  
```pip install -r requirements.txt```

## Environment variables: 
Create file  ```.env``` with you dvmn.org TOKEN, TELEGRAM_BOT_TOKEN, CHAT_ID.  
Like this:  
```
TOKEN="Token 8e64"  
TELEGRAM_BOT_TOKEN="90303613:AA353458O4"  
CHAT_ID="315552"
```  

## Run              
Execute this script in CMD.
For example:  
```python dvmn_chat_bot.py```

Notification will be send to you in telegram if task will be checked.
