from pysimverse import Drone
import time

#initialization
drone = Drone()
drone.connect()
drone.take_off()

#constants
left_right = 0
forward_backward = 250
up_down = 250
yaw = 0

while True:
    drone.send_rc_control(left_right,forward_backward,up_down, yaw)


drone.land()
time.sleep(1)
