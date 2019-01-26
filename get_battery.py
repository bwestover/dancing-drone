import tello

drone = tello.Tello('192.168.10.2', 8888)

print drone.get_battery()
