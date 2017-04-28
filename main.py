from allegro import Allegro

import cloghandler
import logging
import logging.config
import time

import argparse


logging.config.fileConfig("logging.ini")
LOG=logging.getLogger("api")

class Overture(object): 
    def __init__(self):
        self.name = "Overture"
        self.app = Allegro("Overture")
        self.app.initialize("api.ini")


    def start(self):
        self.app.start()
   

    def stop(self):
        self.app.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Two actions are supported {stop | start}.")
    args = parser.parse_args()
    app = Overture()
    if args.action == "start" or args.action == "stop":
        command = "app.%s()" % action
        eval(command)
    else:
        raise AttributeError("The action(%s) is not supported." % args.action)
