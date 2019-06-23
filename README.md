# led-status
This project uses:
1. Raspberry Pi B+
2. remote control no-name Car MP3 (this is what it's written on it)
3. IR receiver
4. RGB LED

...to create a kind of "status" indicator.  
You can set the hardware on your desk and, using the remote, turn the color of the LED to red, yellow, green to indicate the status (for example, RED = do not disturb, YELLOW = disturb only for special occasions, GREEN = anyone can interrupt you).  
For how to wire the things see the attached pictures in ./images and, of course, the code.
A map to GPIO pins will be added soon.

## Install
NOTE: Installing all the dependencies is a __HORROR__ because Raspbian Stretch introduced a so called "disruptive" change vs. Raspbian Jessie.
### lirc  
`sudo apt-get install lirc`  
[This](https://github.com/mtraver/rpi-ir-remote) tutorial helped but see also the modified system files (in ./system folder):
- config.txt goes into /boot/config.txt. What is important is line `dtoverlay=gpio-ir,gpio_pin=18`
- lirc_options.conf goes into /etc/lirc/lirc_options.conf. The important lines are `driver = default` and `device = /dev/lirc0`.
- lircd.conf goes into /etc/lirc/lircd.conf. This file is specific to the remote control used (in this case Car MP3).
### python3-lirc
`sudo apt-get install python3-lirc`
### Neopixel
`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`
## Run
`sudo python3 ./status.py`
## Use
Click the following buttons on remote:
- 0 = RED
- 1 = YELLOW
- 2 = GREEN
- 9 = Alarm RED (press any other key to turn off)
- CH- = Alarm WHITE (press any key to turn off)
- CH = OFF
