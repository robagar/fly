from threading import Thread
from time import sleep
from djitellopy import Tello

tello = Tello()

def output_state():
    try:
        h = tello.get_height()
        print(f'height: {h}')
    except:
        pass

def poll_and_output_state():
    output_state()    
    sleep(1)

output_state_thread = Thread(target=poll_and_output_state, daemon=True)
output_state_thread.start()

tello.connect()
tello.takeoff()

#tello.move_left(100)
#tello.rotate_counter_clockwise(90)
tello.move_forward(50)

tello.land()