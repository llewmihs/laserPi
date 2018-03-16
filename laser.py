import time
import explorerhat

threshold = 2.5
delay = 0.25



while True:
    Voltage1  = explorerhat.analog.four.read()
    print('Voltage is %d' % Voltage1)
    if V2 > threshold:
        explorerhat.output.one.off()
        explorerhat.output.two.on()
    else:
        explorerhat.output.one.on()
        explorerhat.output.two.off()        
    time.sleep(delay)