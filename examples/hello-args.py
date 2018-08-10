#!/usr/bin/env python

import signal
import sys
import time

import scrollphathd

print("""
Scroll pHAT HD: Hello Args

Scrolls a message across the screen that's passed
in as an argument when the script is run. E.g:

python hello-args.py "Hello World"

Press Ctrl+C to exit!

""")

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
#scrollphathd.rotate(degrees=180)

# Write the "Hello World!" string in the buffer and
#   set a more eye-friendly default brightness
scrollphathd.write_string(sys.argv[1], brightness=0.5)

# Auto scroll using a while + time mechanism (no thread)
while True:
    # Show the buffer
    scrollphathd.show()
    # Scroll the buffer content
    scrollphathd.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
