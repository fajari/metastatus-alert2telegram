import requests
import xml.etree.ElementTree as ET
from telegram.bot import Bot

# Send a request to the website and retrieve the data
response = requests.get('https://metastatus.com/outage-events-feed-waba.rss')
data = response.text

# Parse the data and extract the information you need
root = ET.fromstring(data)

# Read the previous_title from the file
with open('previous_title.txt', 'r') as f:
    previous_title = f.read()

for item in root.findall('./channel/item'):
    title = item.find('title').text
    #description = item.find('description').text
    pubDate = item.find('pubDate').text
    print(title)
    #print(description)
    print(pubDate)

# Send a message to Telegram
    if title != previous_title:
        # put your bot id and chat id here
        bot = Bot('xxxxxxxxxx')
        chat_id = xxxxxxxxxxx
        message = f"{title}\n{pubDate}"
        bot.send_message(chat_id=chat_id, text=message)

    # Update the previous title
    with open('previous_title.txt', 'w') as f:
        f.write(title)
