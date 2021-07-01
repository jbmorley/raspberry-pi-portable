# Raspberry Pi Portable

Raspberry Pi based portable device

## Hardware

- [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)
- [Pimoroni HyperPixel 4.0 Square](https://shop.pimoroni.com/products/hyperpixel-4-square?variant=30138251444307)
- [Adafruit PowerBoost 1000 Charger](https://www.adafruit.com/product/2465)
- [ATXRaspi R3](https://lowpowerlab.com/shop/product/91)

## Configuration

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

3. Install the HyperPixel driver (https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4).

   ```bash
   curl https://get.pimoroni.com/hyperpixel4 | bash
   ```

4. Install the Python USB libraries for communicating with the GPIO expansion board (https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/linux).

   ```bash
   sudo apt-get install --yes libusb-1.0
   ```
   
   Install the udev rules.
   
   ```bash
   curl https://raw.githubusercontent.com/jbmorley/raspberry-pi-portable/main/11-ftdi.rules | sudo tee /etc/udev/rules.d/11-ftdi.rules 
   ```
   
   Install the Python FTDI library.
   
   ```bash
   pip3 install pyusb
   pip3 install pyftdi
   ```

