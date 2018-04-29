# mock_picamera
A mock Raspberry Pi picamera library for developing code before deploying to a Pi. This is not intended for use as part of automated testing. It is intended to allow applications utilising the picamera library to:
1. Build, run and start up without being installed on a Raspberry Pi
1. Reduce development time by replicating the most commonly-used behaviour of the picamera module  

## Rationale
My interaction with the Raspberry Pi is as limited as I can possibly make it, ideally limited to opening an SSH connection and doing a `git pull`. While Raspberry Pis are great, they just aren't powerful enough to do full development using an IDE (at least not the original Pi that I have). That's fine for the most part, since Python is cross platform so I can get the majority of my apps running just fine on my PC. But when it comes to the Pi Camera, there is no alternative to just pushing the code to the Pi for testing. This makes for a very slow development process. This package aims to address this gap. While a mock picamera module will never be a full substitute for proper testing with a real camera on the Pi, I hope it will reduce development time.

## Current Development Status
This project has only just begun and is currently immature (to the point of being fairly useless).

