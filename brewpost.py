import requests
import time
import TiltHydrometer


tiltcolor = "Red"

myurl = open("url","r")
myurl = myurl.readline()

beerinprogress = open("beerinprogress", "r")
beerinprogress = beerinprogress.readline()

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

payload = {
"Timepoint": "=NOW()",
"SG": readings[1],
"Temp": readings[0],
"Color": tiltcolor.upper(),
"Beer": beerinprogress,
"Comment": ""
}


def post_data(payload):
    requests.post(url=myurl, data=payload)

post_data(payload)


#post_data = {'Timepoint':'=NOW()', 'SG':'0.6'}
# POST some form-encoded data:
#post_response = requests.post(url=myurl, data=post_data)
