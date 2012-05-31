__author__="ICP(ivanhaleh@gmail.com)"
__date__ ="$02-may-2012 17:12:56$"

import threading
import time

class XTimer():
    def __init__(self, time, onTimer, params = None, count = -1):
        self.time = time
        self.onTimer = onTimer
        self.params = params
        self.count = count
        self.counter = 0
        self.init()

    def init(self):
        self.state = "initializing"

    def pause(self):
        self.state = "paused"

    def run(self):
        if (self.state != "terminated"):
            self.state = "running"
        else:
            del self.thread
            self.init()
            self.start()

    def terminate(self):
        self.state = "terminated"

    def start(self):
        if (self.state == "initializing"):
            self.run()
            self.thread = threading.Thread(target = self.do, args = ())
            self.thread.start()

    def do(self):
        while (self.state == "running"):
            time.sleep(self.time)
            if (self.state == "running"):
                if (self.params != None):
                    self.onTimer(self.params)
                else:
                    self.onTimer()
                self.counter += 1
                if (self.count > 0 and self.counter >= self.count):
                    self.counter = 0
                    self.state = "exit"
        self.terminate()

if __name__ == "__main__":
   pass