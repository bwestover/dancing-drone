import tello

#connect tello to control device using an IP address as first argument in string format and a secondary input as a Port number. 
drone = tello.Tello('192.168.10.2', 8888)

#as per DJI api, this function allows the drone to take off and hover
drone.takeoff()


#as per DJI api, this function allows the drone to turn on video feed
drone.stream_on()


#as per DJI api, this function allows the drone to go to a given coordinate set in centimetersalong with a given speed from 0-100 (x, y, z, speed)
drone.go_to_coord(100,100,100,99)
drone.go_to_coord(100,100,100,99)
drone.go_to_coord(-100,-100,-100,99)
drone.go_to_coord(100,100,100,99)
drone.go_to_coord(-100,-100,-100,99)

#as per DJI api, this function allows the drone to begin landing procedure at speed 20. Downward facing imaging is disabled here; a flat surface will help.
drone.land()
