#!/bin/bash

# Install and configure the GPIO expansion board.
# https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/linux
sudo apt-get install --yes libusb-1.0
curl https://raw.githubusercontent.com/jbmorley/raspberry-pi-portable/main/11-ftdi.rules | sudo tee /etc/udev/rules.d/11-ftdi.rules 

# Install the Python requirements.
pip3 install -r requirements.txt
