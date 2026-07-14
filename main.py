from pysimverse import Drone
import time

#initialization
drone = Drone()
drone.connect()
drone.take_off()

drone.move_down(20)
time.sleep(2)
drone.move_up(30)
time.sleep(2)

drone.land()
time.sleep(1)
