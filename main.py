from pysimverse import Drone
import time

#initialization
drone = Drone()
drone.connect()
drone.take_off()

#drone.move_forward(80)
#time.sleep(2)
#drone.move_backward(50)
#time.sleep(2)

drone.set_speed(150)
drone.move_forward(80)


drone.land()
time.sleep(1)
