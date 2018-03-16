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
print("Average light is at %f" % firstLight)

while True:
    newLight  = explorerhat.analog.four.read()
    if newLight > firstLight*1.5:
        millis = int(round(time.time()*1000))
        print("Ping")
        time.sleep(0.5)
        while True:
            newLight  = explorerhat.analog.four.read()
            if newLight > firstLight*1.5:
                print("Pong")
                sailTime = int(round(time.time()*1000)) - millis
                print("Time: %f" % sailTime/1000)
                time.sleep(0.5)
                break      