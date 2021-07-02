#!/usr/bin/env python3

import subprocess
import time

import board
import digitalio


def main():

    boot_ok = digitalio.DigitalInOut(board.C0)
    boot_ok.direction = digitalio.Direction.OUTPUT

    # Reset the board by toggling the the boot OK signal
    boot_ok.value = False
    time.sleep(0.1)
    boot_ok.value = True

    shutdown = digitalio.DigitalInOut(board.C1)
    shutdown.direction = digitalio.Direction.INPUT

    software_shutdown = digitalio.DigitalInOut(board.C2)
    software_shutdown = digitalio.Direction.OUTPUT
    software_shutdown.value = True

    lbo = digitalio.DigitalInOut(board.C3)
    lbo.direction = digitalio.Direction.INPUT

    while True:
        print(shutdown.value, lbo.value)
        time.sleep(0.1)

        if shutdown.value:
            time.sleep(0.1)
            boot_ok.value = False
            subprocess.check_call(["sudo", "shutdown", "now"])


if __name__ == "__main__":
    main()
