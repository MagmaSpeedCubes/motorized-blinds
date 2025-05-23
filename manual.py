from gpiozero import Servo
from time import sleep

SPIN_TIME = 5

servo = Servo(18, min_pulse_width=500/1_000_000, max_pulse_width=2500/1_000_000)



def open_blinds():

    print("Opening blinds")
    servo.value = -1
    sleep(SPIN_TIME)
    servo.value = 0
    print("Opened blinds")

def close_blinds():
    print("Closing blinds")
    servo.value = 1
    sleep(SPIN_TIME)
    servo.value = 0
    print("Closed blinds")

