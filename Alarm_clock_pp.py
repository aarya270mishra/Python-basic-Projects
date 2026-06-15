
from playsound import playsound 
import time 


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60 

        print(f"\rAlarm Will Sound in : {minutes_left:02d}:{seconds_left:02d}   " , end="") 

    playsound(r"C:\Users\AARYA\Downloads\mixkit-facility-alarm-sound-999.wav")


minute = int(input("How many minutes to wait ?"))
seconds = int(input("How many Seconds ?"))
total_time = minute * 60 + seconds          
alarm(total_time)


