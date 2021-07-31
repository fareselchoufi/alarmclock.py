# Build alarm clock using Python
from datetime import datetime


alarm_time = input("Enter time in 'HH:MM:SS AM/PM format")

def verify_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again"
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid hour format! Please try again"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE forat! Please try again"
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again"
        else:
            return "OK"

while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

    verify = verify_time(alarm_time.lower())
    if verify != "ok":
        print(verify)
    else:
        print(f"Setting alarm for {alarm_time}")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

now = datetime.now()

current_hour = now.strftime("%I)")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")

if alarm_period == current_period:
    if alarm_hour == current_hour:
        if alarm_min == alarm_min:
            if alarm_sec == alarm_sec:
                print("Wake Up!!!")


while True:
    now = datetime.now()

    current_hour = now.strftime("%I)")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == alarm_min:
                if alarm_sec == alarm_sec:
                    print("Wake Up!!!")


