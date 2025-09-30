import os
import requests
from datetime import date

def sms_alert(body, to):
    # Using Textbelt
    text_belt_api_key = os.getenv("TEXT_BELT_API_KEY")
    print(type(text_belt_api_key))
    resp = requests.post('https://textbelt.com/text', {
      'phone': to,
      'message': body,
      'key': text_belt_api_key,
    })

def Tn(n):
    sum = 0
    for x in range(1,n+1):
        sum = sum + x
    return sum

day = date.today().day
day_of_week = date.today().weekday()

squat_num = Tn(day)

if __name__ == '__main__':
    if(day == 31):
        daily_message = f"1️⃣🥇💯Last day!!! gotta do {squat_num} squats, 👻happy halloween!🧟🧛🧌🕸️🕷️☠️👻👺"
    elif(day == 30):
        daily_message = f"2️⃣🥈🥈Second to last day!! gotta do {squat_num} squats🎃🎃🏋️"
    elif(day == 29):
        daily_message = f"3️⃣🥉🥉🥉Third to last day!! gotta do {squat_num} squats🐂"
    elif(day == 16):
        daily_message = f"🕤Over half way there🕞!! you can do it💪💪💪, {squat_num} squats"
    elif(day == 8):
        daily_message = f"🦊🦊🦊One week down!! gotta do {squat_num} squats🫏🫏🫏"
    elif(day == 1):
        daily_message = f"Happy Squatober🎃🎃! each day for the month of October you will be sent a message with an increasing number of bodyweight-squats to do, we're starting with {squat_num} squat for the first day of this quad busting journey🏋️"
    elif(day_of_week == 0):
        daily_message = f"🍝🍝{squat_num} monday squats, do it for Garfield! :3🐈🐈🐈"
    elif(day_of_week == 1):
        daily_message = f"{squat_num} squats today, 🚂Tues🚃🚎🚡🚃 many but you can do it!🦛🦧🦏🦍"
    elif(day_of_week == 2):
        daily_message = f"Get over the 🐪hump🐫 day, {squat_num} squats🐒!"
    elif(day_of_week == 4):
        daily_message = f"🎈🎈Happy friday🎊🎊! You got {squat_num} squats to do :> 🕺🪩"
    elif(day_of_week == 5):
        daily_message = f"🏢Work is done, 🏫school is out but it's time to do {squat_num} squats🏋️"
    elif(day_of_week == 6):
        daily_message = f"It may be the ⛪Sabbath🦾🧑‍🏭! But you got {squat_num} squats to do."
    else:
        daily_message = f"You gotta do {squat_num} squats today, good luck!"

    phone_numbers = os.getenv("PHONE_NUMBERS", "").split(",")
    for phone in phone_numbers:
        if phone.strip():
            sms_alert(daily_message, phone.strip())
