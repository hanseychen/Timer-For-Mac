import os
import sys
import time


# Print the usage of the timer
def print_usage():
    print("usage: timer.py <number of minutes>")


# Main Functionality
# Check argument numbers
if len(sys.argv) != 2:
    print_usage()

# Check argument range
minutes = int(sys.argv[1])
if minutes > 60 or minutes < 1:
    print("Please specify time between 1 minute and 60 minutes.")

# Do count down
time.sleep(minutes * 60)
os.system('say "your timer has expired"')
