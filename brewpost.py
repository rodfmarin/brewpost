import requests
import TiltHydrometer


myurl = open("url","r")
myurl = myurl.readline()

tiltHydrometer = TiltHydrometer.TiltHydrometerManager(False, 60, 40)
tiltHydrometer.loadSettings()
tiltHydrometer.start()

for color in TiltHydrometer.TILTHYDROMETER_COLOURS:
    print color + ": " + str(tiltHydrometer.getValue(color))

tiltHydrometer.stop()








#post_data = {'Timepoint':'=NOW()', 'SG':'0.6'}
# POST some form-encoded data:
#post_response = requests.post(url=myurl, data=post_data)
