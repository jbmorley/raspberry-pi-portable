# Raspberry Pi Portable

Raspberry Pi based portable device

## Hardware

- [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)
- [Pimoroni HyperPixel 4.0 Square](https://shop.pimoroni.com/products/hyperpixel-4-square?variant=30138251444307)

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

3. Install the HyperPixel driver.

   ```bash
   curl https://get.pimoroni.com/hyperpixel4 | bash
   ```
