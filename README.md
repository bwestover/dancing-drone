# Drone controller

To test receiving the video stream, you can use ffplay:

```
ffplay -probesize 32 -i udp://@:11111 -framerate 30
```

This sets up a local udp server and displays the video stream that it receives. The Tello sends its video stream on `UDP:11111`
