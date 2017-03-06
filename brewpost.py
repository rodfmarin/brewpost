import requests
import time
import TiltHydrometer


tiltcolor = "Red"

myurl = open("url","r")
myurl = myurl.readline().rstrip()

beerinprogress = open("beerinprogress", "r")
beerinprogress = beerinprogress.readline().rstrip()

def getTiltReadings(sleepseconds):
    # Connection to the Tilt takes a few seconds to get a reading
    # sleepseconds  ensures we will not  return 'None' by trying to read
    # before a connection is established
    # returns the Temp and SG readings from the tilt
    tiltHydrometer = TiltHydrometer.TiltHydrometerManager(False, 60, 40)
    tiltHydrometer.loadSettings()
    tiltHydrometer.start()
    time.sleep(sleepseconds)

    values = tiltHydrometer.getValue(tiltcolor)

    return values.temperature, values.gravity


readings = getTiltReadings(10)

mypayload = {
"Timepoint": "=NOW()",
"SG": readings[1],
"Temp": readings[0],
"Color": tiltcolor.upper(),
"Beer": beerinprogress,
"Comment": ""
}

print mypayload

def post_data(payload):
    requests.post(url=myurl, data=payload)

try:
    post_data(mypayload)
except Exception as e:
    print e
    raise





#post_data = {'Timepoint':'=NOW()', 'SG':'0.6'}
# POST some form-encoded data:
#post_response = requests.post(url=myurl, data=post_data)
