import os
import vonage
from datetime import date

def sms_alert(body, to):
    # SignalWire credentials
    project_id = os.getenv("VONAGE_API")
    api_token = os.getenv("VONAGE_KEY")
    from_number = os.getenv("VONAGE_NUMBER")  # Your purchased SignalWire number

    client = vonage.Client(key=project_id, secret=api_token)
    sms = vonage.Sms(client)
    
    responseData = sms.send_message(
        {
            "from": from_number,
            "to": to,
            "text": "A text message sent using the Nexmo SMS API",
        }
    )
    
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

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
        daily_message = f"Last day!!! gotta do {squat_num} squats, happy halloween!"
    elif(day == 30):
        daily_message = f"Second to last day!! gotta do {squat_num} squats"
    elif(day == 29):
        daily_message = f"Third to last day!! gotta do {squat_num} squats"
    elif(day == 16):
        daily_message = f"Over half way there!! you can do it, {squat_num} squats"
    elif(day == 8):
        daily_message = f"One week down!! gotta do {squat_num} squats"
    elif(day_of_week == 0):
        daily_message = f"{squat_num} monday squats, do it for Garfield! :3"
    elif(day_of_week == 1):
        daily_message = f"{squat_num} squats today, Tues many but you can do it!"
    elif(day_of_week == 2):
        daily_message = f"Get over the hump day, {squat_num} squats!"
    elif(day_of_week == 4):
        daily_message = f"Happy friday! You got {squat_num} squats to do :>"
    elif(day_of_week == 5):
        daily_message = f"Work is done, school is out but it's time to do {squat_num} squats."
    elif(day_of_week == 6):
        daily_message = f"It may be the Sabbath! But you got {squat_num} squats to do."
    else:
        daily_message = f"You gotta do {squat_num} squats today, good luck!"

    phone_numbers = os.getenv("PHONE_NUMBERS", "").split(",")
    for phone in phone_numbers:
        if phone.strip():
            sms_alert(daily_message, phone.strip())
