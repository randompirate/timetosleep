# timetosleep
Small utility to sleep until sunset in a given location. Usage with cron.


# Motivation:
Crontab has no native '@sunset' identifier. Use this script to pause until sunset and then start the script you wish to run:
timetosleep.py; script-to-run.sh

# Usage:
timetosleep.py \[positive/negative offset in minutes\] \[sunrise|sunset\]

