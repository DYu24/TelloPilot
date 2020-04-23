import av
import cv2.cv2 as cv2
import numpy as np
import sys
import tellopy
import time
import threading
import pygame
from controllers.keyboard import Keyboard

image = None

def flight_handler(event, sender, data, **args):
    if event is sender.EVENT_FLIGHT_DATA:
        print(data)
    
def video_thread(drone):
    try:
        container = av.open(drone.get_video_stream())

        frame_skip = 300
        while True and container:
            for frame in container.decode(video=0):
                if frame_skip > 0:
                    frame_skip -= 1
                    continue
    
                start_time = time.time()
                image = cv2.cvtColor(np.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                cv2.imshow('Tello', image)
                cv2.waitKey(1)

                if frame.time_base < 1 / 60:
                    time_base = 1 /60
                else:
                    time_base = frame.time_base
                
                frame_skip = int((time.time() - start_time) / time_base)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    pygame.init()
    pygame.display.init()
    
    drone = tellopy.Tello()

    try:
        # Print flight data to console
        drone.subscribe(drone.EVENT_FLIGHT_DATA, flight_handler)
        
        # Connect to drone
        drone.connect()
        drone.wait_for_connection(30)

        # Setup keyboard to control the drone
        controller = Keyboard(drone)
        speed = 50

        # Start listening to the drone's video stream
        threading.Thread(target=video_thread, args=[drone]).start()

        while True:
            time.sleep(0.01)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                    
                if event.type == pygame.KEYDOWN:
                    if pygame.key.name(event.key) == 'escape':
                        exit(0)
                    controller.handleInput(pygame.key.name(event.key), speed)
                elif event.type == pygame.KEYUP:
                    controller.handleInput(pygame.key.name(event.key), 0)

    except Exception as e:
        print(e)

    finally:
        drone.quit()
        cv2.destroyAllWindows()
