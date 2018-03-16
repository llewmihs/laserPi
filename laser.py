import time
import explorerhat

threshold = 2.5
delay = 0.25

def getAveLight():
    aveVolts = 0
    for i in range(10):
        aveVolts = aveVolts + explorerhat.analog.four.read()
        time.sleep(0.1)
    return aveVolts/10

firstLight =  getAveLight()   
print("Average light is at %f" firstLight)

while True:
    newLight  = explorerhat.analog.four.read()
    if newLight > firstLight*1.2:
        print("Ping")
    # if V2 > threshold:
    #     explorerhat.output.one.off()
    #     explorerhat.output.two.on()
    # else:
    #     explorerhat.output.one.on()
    #     explorerhat.output.two.off()        
    time.sleep(delay)