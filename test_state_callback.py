from djitellopy import Tello

tello = Tello()

def on_state_received(drone_address, state):
    print(f'state received from {drone_address}')
    for k,v in state.items():
        print(f'  {k}: {v}')

Tello.on_state_received = on_state_received

tello.connect()
tello.takeoff()

for i in range(4):
    tello.move_forward(50)
    tello.rotate_counter_clockwise(90)

tello.land()