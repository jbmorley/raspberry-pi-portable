#!/bin/bash

# Ensure the Raspberry Pi is up to date.
sudo apt-get update
sudo apt-get --yes upgrade
sudo apt-get --yes autoremove

# Install some useful additional software.
# N.B. This step is entirely optional but helps set up devices for development.
sudo apt-get install --yes \
     mosh \
     emacs

# Install and configure the GPIO expansion board.
# https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/linux
sudo apt-get install --yes \
     libusb-1.0
sudo cp 11-ftdi.rules /etc/udev/rules.d/11-ftdi.rules

# Install the Python requirements.
pip3 install -r requirements.txt
