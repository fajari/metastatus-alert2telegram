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

1. Save file metastatus_alert2telegram.py to your script folder, for example /home/user/script/

2. Run the script :
   python metastatus_alert2telegram.py

3. If you want to monitor metastatus frequently, you can add it on crontab, for example :

*/5 * * * * cd /home/user/script/; python metastatus_alert2telegram.py


# Version:
v0.0.1
