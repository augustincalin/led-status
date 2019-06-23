import lirc
import time
 
sockid = lirc.init("pylirc", "./conf")
 
while True:
    codeIR = lirc.nextcode()
    if codeIR != []:
        print(codeIR[0])
    time.sleep(0.05)