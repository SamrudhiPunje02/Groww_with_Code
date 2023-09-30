import time
from playsound import playsound

def set_alarm():
    Hour_hand = int(input("Type hour (24-hour format): "))
    minutes_hand = int(input("Type minute: "))
    return Hour_hand, minutes_hand

def start_alarm(Hour_hand, minutes_hand):
    while True:
        Actual_time = time.localtime()
        if Actual_time.tm_hour == Hour_hand and Actual_time.tm_min == minutes_hand:
            print("Time's up! Alarm ringing...")
            playsound("E:\WhatsApp Audio 2023-09-25 at 00.46.33.mp3") 
            break
        time.sleep(60) 

if __name__ == "__main__":
    print("SET ALARM TO : ")
    alarm_hours, alarm_minutes = set_alarm()
    start_alarm(alarm_hours, alarm_minutes)
