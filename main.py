from pysimverse import Drone
import time

#initialization
drone = Drone()
drone.connect()
drone.take_off()

drone.move_left(20)
time.sleep(2)
drone.move_right(30)
time.sleep(2)

drone.land()
time.sleep(1)
