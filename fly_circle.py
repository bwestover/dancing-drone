import tello

drone = tello.Tello('192.168.10.2', 8888)

drone.takeoff()
drone.stream_on()

drone.go_to_coord(0,50,50,99)
drone.go_to_coord(0,0,50,99)
drone.go_to_coord(0,-50,50,99)
drone.go_to_coord(0,-50,0,99)
drone.go_to_coord(0,-50,-50,99)
drone.go_to_coord(0,0,-50,99)
drone.go_to_coord(0,50,-50,99)
drone.go_to_coord(0,50,0,99)

drone.land()
