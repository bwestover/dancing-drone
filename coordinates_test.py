import tello

drone = tello.Tello('192.168.10.2', 8888)

drone.takeoff()
drone.stream_on()
drone.go_to_coord(100,100,100,99)
drone.go_to_coord(-100,-100,-100,99)
drone.go_to_coord(100,100,100,99)
drone.go_to_coord(-100,-100,-100,99)
drone.go_to_coord(100,100,100,99)
drone.go_to_coord(-100,-100,-100,99)
drone.land()
