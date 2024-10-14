import os
import smtplib
from email.message import EmailMessage
from datetime import date

def email_alert(body, to):
    msg = EmailMessage()
    msg.set_content(body)  # Only set the body, no subject

    user = "stanleygarbagea@gmail.com"
    msg['from'] = "Squatober Alert"
    msg['to'] = to    
    password = "vizwosvmrdjtgrye"  # Your app password

    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def Tn(n):
    sum = 0
    for x in range(1,n+1):
        sum = sum + x
    return sum

day = date.today().day
day_of_week = date.today().weekday()
# print(day_of_week)
# get mon, tue, wed, etc from it

squat_num = Tn(day)
# print(test)

if __name__ == '__main__':
    if(day == 31):
        daily_message = f"Last day!!! gotta do {squat_num} squats, happy halloween!"
    elif(day == 30):
        daily_message = f"Second to last day!! gotta do {squat_num} squats"
    elif(day == 29):
        daily_message = f"Third to last day!! gotta do {squat_num} squats"
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
#     # email_alert("Hey", "I'm sending this via a program", "4199022677@vtext.com") #Verizon
    phone_numbers = os.getenv("PHONE_NUMBERS", "").split(",")
    for phone in phone_numbers:
        email_alert(daily_message, phone)