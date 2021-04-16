from threading import Thread
from time import sleep
from djitellopy import Tello

tello = Tello()

def output_state():
    s = tello.get_current_state()
    print('state:')
    for k,v in s.items():
        print(f'  {k}: {v}')

def poll_and_output_state():
    while True:
        output_state()    
        sleep(1)

output_state_thread = Thread(target=poll_and_output_state, daemon=True)
output_state_thread.start()

tello.connect()
tello.takeoff()

for i in range(4):
    tello.move_forward(50)
    tello.rotate_counter_clockwise(90)

tello.land()