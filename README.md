Notification telegram bot
=====================
 
This script send notification about checked tasks on dvmn.org

Python3 should be installed.  
Use pip to install dependencies:  
```pip install -r requirements.txt```

How to use this script:  
* Create file  ```.env``` with you dvmn.org token, telegram bot token, chat id.  
Like this: ```token="Token 8e64"  
              telegramBotToken="90303613:AA353458O4"  
              chat_id="315552"```  
* Execute this script in CMD.
For example:  
```ChatBot.py"```

Script will work 100 sec. Notification will be send to you in telegram if task will be checked during this time.
