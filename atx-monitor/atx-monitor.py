#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import sys
import time

import jinja2

import cli


ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIRECTORY = os.path.join(ROOT_DIRECTORY, "templates")

SERVICE_NAME = "atx-monitor.service"

ATX_MONITOR_PATH = os.path.join(ROOT_DIRECTORY, "atx-monitor", "atx-monitor")
SERVICE_PATH = os.path.join("/etc/systemd/system", SERVICE_NAME)


verbose = '--verbose' in sys.argv[1:] or '-v' in sys.argv[1:]
logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO, format="[%(levelname)s] %(message)s")


@cli.command("install")
def command_install(options):
    logging.info("Installing...")

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIRECTORY))
    template = environment.get_template("atx-monitor.service")

    with open(SERVICE_PATH, "w") as fh:
        fh.write(template.render(path=ATX_MONITOR_PATH))

    logging.info("Reloading systemd...")
    subprocess.check_call(["systemctl", "daemon-reload"])

    logging.info("Enabling and starting service...")
    subprocess.check_call(["systemctl", "enable", SERVICE_NAME])
    subprocess.check_call(["systemctl", "start", SERVICE_NAME])

    logging.info("Done.")


@cli.command("log")
def command_log(options):
    subprocess.run(["journalctl", "-u", SERVICE_NAME, "-f"])


@cli.command("monitor")
def command_monitor(options):

    import board
    import digitalio
    
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


def main():
    parser = cli.CommandParser()
    parser.add_argument('--verbose', '-v', action='store_true', default=False, help="show verbose output")
    parser.run()


if __name__ == "__main__":
    main()
