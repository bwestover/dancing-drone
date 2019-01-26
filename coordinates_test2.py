import tello

drone = tello.Tello('192.168.10.2', 8888)

drone.takeoff()
drone.stream_on()

drone.curve_to_coord(0,0,0,0,50,50,59)
drone.curve_to_coord(0,0,0,0,-50,50,59)
drone.curve_to_coord(0,0,0,0,-50,-50,59)
drone.curve_to_coord(0,0,0,0,50,-50,59)



drone.land()
