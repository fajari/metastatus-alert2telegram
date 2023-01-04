# metastatus-alert2telegram
# DevOps Tools / System Administrator Tools

This script created to monitor metastatus (waba) outage event. Website to monitor is : https://metastatus.com/outage-events-feed-waba.rss
Every change on that rss will send alert to telegram


# Requirements
This package needs:
- Python 3.11.x
- Telegram.bot
- Requests
- xml.etree.ElementTree

# How To Use

1. Copy scrips ./scripts/* to your script folder, for example /home/user/script/
2. Create a empty file on that same folder with script (/home/user/script/): previous_title.txt if not exists on /scripts/ folder
3. Change the bot_id and chat_id to your own chat_id and bot_id. Ask bot_father on telegram about it.
   bot = Bot('xxxxxxxxxx')
   chat_id = xxxxxxxxxxx
6. Run the script :
   python check_metastatus.py
7. If you want to monitor metastatus frequently, you can add it on crontab, for example :

   */5 * * * * cd /home/user/script/; python check_metastatus.py


# Version:
v0.0.1
