import time
import board
import analogio
import neopixel
# Create an analog input for the light sensor
light = analogio.AnalogIn(board.LIGHT)
# Set up the NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
# Function to convert raw sensor data to voltage
def get_voltage(pin):
    return (pin.value * 3.3) / 65536
while True:
    light_level = get_voltage(light)
    print("Light level:", light_level)
    # If it's bright, turn on the NeoPixels white, else turn them off
    if light_level > 1.5:
        pixels.fill((255, 255, 255))  # White if bright
    else:
        pixels.fill((0, 0, 0))  # Off if dark
    time.sleep(0.1)