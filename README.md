# led-status
This project uses:
1. Raspberry Pi B+
2. remote control
3. IR receiver
4. RGB LED

...to create a kind of "status" indicator.  
You can set the hardware on your desk and, using the remote, set the color of the LED to red, yellow, green to indicate the status (red = do not disturb, yellow = disturb only for special occasions, green = ok, you can disturb).  
For how to wire the things see the attached pictures and, of course, the code.

##Install
1. lirc
`sudo apt-get install lirc`
2. change modules
add  
lirc_dev  
lirc_rpi gpio_out_pin=22  
...to `sudo nano /etc/modules`  
3. more changes  
sudo nano  /etc/lirc/hardware.conf
and add
LIRCD_ARGS="--uinput"
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
LIRCD_CONF=""
LIRCMD_CONF=""