from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

def capture_video():
    try:
        while True:
            print('waiting for video frame...')
            frame = frame_read.frame
            # print(f'frame: {frame}')
            print('frame!')
    except e:
        print(f'video capture error: {e}')

capture_video_thread = Thread(target=capture_video, daemon=True)
capture_video_thread.start()

