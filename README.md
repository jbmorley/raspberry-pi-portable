# Raspberry Pi Portable

Raspberry Pi based portable device

## Overview

There are many Raspberry Pi portables out there--I wanted to make one of my own using the Pimoroni 4" square capacitive touch screen display. I'm thinking of building a media remote that displays the artwork for the current album, or using it to revisit a virtual pet project I worked on many years ago (https://jbmorley.co.uk/posts/2006-08-18-nezumi/).

## Hardware

- [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)
- [Pimoroni HyperPixel 4.0 Square](https://shop.pimoroni.com/products/hyperpixel-4-square?variant=30138251444307)
- [Adafruit PowerBoost 1000 Charger](https://www.adafruit.com/product/2465)
- [Adafruit FT232H Breakout](https://www.adafruit.com/product/2264)
- [ATXRaspi R3](https://lowpowerlab.com/shop/product/91)

## Software

1. Ensure Raspbian is up to date.

   ```bash
   sudo apt-get update
   sudo apt-get --yes upgrade
   sudo apt-get --yes autoremove
   ```

2. [Mosh](https://mosh.org/) is useful to have around in case your laptop goes to sleep during the rest of the process or your on an unreliable network.

   ```bash
   sudo apt-get install --yes mosh
   ```

   You can reconnect to your Raspberry Pi using Mosh as follows:
   
   ```bash
   mosh pi@raspberrypi.local
   ```

4. Install the HyperPixel driver (https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4).

   ```bash
   curl https://get.pimoroni.com/hyperpixel4 | bash
   ```
   
5. Clone the project and run the install script.

   ```bash
   git@github.com:jbmorley/raspberry-pi-portable.git
   cd reaspberry-pi-portable
   ./install.sh
   ```
      
6. Check out that the IO code is running correctly.

   ```python
   #!/usr/bin/env python3

   import time

   import board
   import digitalio


   def main():

       button = digitalio.DigitalInOut(board.C1)
       button.direction = digitalio.Direction.INPUT

       while True:
           print(button.value)
           time.sleep(1)


   if __name__ == "__main__":
       main()
   ```
   
7. Enable the service.

   ```bash
   sudo systemctl enable atx-monitor.service
   sudo systemctl start atx-monitor.service
   ```
   
8. Check the service is running.

   ```bash
   journalctl -u atx-monitor.service -f
   ```

9. Reboot.

## Notes

- Some good systemd documentation at https://www.raspberrypi.org/documentation/linux/usage/systemd.md, and an example of the various phases on https://github.com/coreos/docs/blob/master/os/getting-started-with-systemd.md#unit-file.
- Right now, it seems that wiring up the soft button to the USB GPIO board causes the ATX board to stop functioning correctly irrespective of how the GPIO is set to that board. It's possible that it needs a pull-down resistor.
