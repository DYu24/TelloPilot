from time import sleep
import tellopy

def subscription_handler(event, sender, data, **args):
    if event is sender.EVENT_FLIGHT_DATA:
        print(data)

if __name__ == '__main__':
    drone = tellopy.Tello()

    try:
        # Print flight data to console
        drone.subscribe(drone.EVENT_FLIGHT_DATA, subscription_handler)
        
        # Connect to drone
        drone.connect()
        drone.wait_for_connection(30)
        
        # Routine
        drone.takeoff()
        sleep(5)
        drone.flip_forward()
        sleep(5)
        drone.down(45)
        sleep(5)
        drone.land()
        sleep(5)
    except Exception as e:
        print(e)
    finally:
        drone.quit()