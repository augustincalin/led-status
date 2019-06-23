# Simple test for NeoPixels on Raspberry Pi
import lirc
import time
import time
import board
import neopixel

sockid = lirc.init("pylirc", "./conf", blocking=False)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D12

# The number of NeoPixels
num_pixels = 1

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

alertMode = False

def busy(pixels):
    pixels.fill((255,0,0))
    pixels.show()

def almostBusy(pixels):
    pixels.fill((255,255,0))
    pixels.show()

def off(pixels):
    pixels.fill((0,0,0))
    pixels.show()

def ok(pixels):
    pixels.fill((0,255,0))
    pixels.show()

def on(pixels):
    pixels.fill((255,255,255))
    pixels.show()

def alert(pixels):
    alertMode = True
    while alertMode:
        code = lirc.nextcode()
        if code != []:
            alertMode = False
        pixels.fill((255,255,255))
        pixels.show()
        time.sleep(1)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

def armagedon(pixels):
    alertMode = True
    while alertMode:
        code = lirc.nextcode()
        if code != []:
            alertMode = False
        for i in range(255):
            pixels.fill((i,0,0))
            pixels.show()
        for i in range(255):
            pixels.fill((255-i,0,0))
            pixels.show()



if __name__=='__main__':
    on(pixels)
    try:
        while True:
            codeIR = lirc.nextcode()
            if codeIR != []:
                print(codeIR[0])
                alertMode = False
                if codeIR[0]=="KEY_NUMERIC_2":
                    ok(pixels)
                elif codeIR[0]=="KEY_NUMERIC_1":
                    almostBusy(pixels)
                elif codeIR[0]=="KEY_NUMERIC_0":
                    busy(pixels)
                elif codeIR[0] == "KEY_CHANNEL":
                    off(pixels)
                elif codeIR[0] == "KEY_CHANNELDOWN":
                    alert(pixels)
                elif codeIR[0] == "KEY_NUMERIC_9":
                    armagedon(pixels)
                
            # else:
                # print("none")

    except KeyboardInterrupt:
        lirc.deinit()
        off(pixels)


