
# Lights on 20 minutes after sunset
0 12 * * * /home/pi/bin/timetosleep.py 20 sunset; /home/pi/bin/PhilipsHue/hue.py on