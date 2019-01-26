import tello

drone = tello.Tello('192.168.10.2', 8888)

#print drone.get_battery()
#print drone.get_battery()
drone.takeoff()
drone.flip('l')
drone.land()
