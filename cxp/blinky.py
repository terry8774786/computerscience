from adafruit_circuitplayground import cp
import time




while True:
    cp.pixels.fill((0 , 30 , 0))
    time.sleep(.367)
    cp.pixels.fill((0, 0, 0))
    time.sleep(.367)