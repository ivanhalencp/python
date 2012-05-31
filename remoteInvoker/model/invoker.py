__author__="ICP(ivanhalen@gmail.com)"
__date__ ="$17-may-2012 14:22:14$"

# PROCESS / PROCESS DEFINITION
import process
# XTIMER / TIMER
import xUtil.xTimer
# XLOGGING / LOGS MANAGER
import xUtil.xLogging
# HTTP COMMUNICATION
import urllib
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError

class Invoker():
    def __init__(self, logToConsole = True, logToFile = False, logFileName = "invoker.log"):
        self.logToConsole = logToConsole
        self.logToFile = logToFile
        self.logFileName = logFileName
        self.logData = ""
        self.fileLogger = None
        self.processes = {}
        self.init_logger()

    def init_logger(self):
        if (self.logToFile):
            self.fileLogger = xUtil.xLogging.XLogging(self.logFileName)

    def get_log(self, clear = False):
        result = self.logData
        if (clear):
            self.logData = ""
        return result

    def read_processes(self, xmlFile):
        pass

    def add_process(self, name, url, time, params = None, sendMethod = "post", resultHandler = None):
        nuProcess = process.Process(name, url, time, params, sendMethod, resultHandler)
        self.processes[name] = nuProcess
        return nuProcess

    def start(self):
        for processName in self.processes:
            process = self.processes[processName]
            xt = xUtil.xTimer.XTimer(process.time, self.invoke, processName)
            xt.start()
            process.timer = xt

    def stop(self):
        for process in self.processes:
            process.timer.terminate()

    def invoke(self, name):
        process = self.processes[name]
        strResult = ""
        if (process != None):
            process.invocations += 1
            try:
                self.log("[Invoking " + str(process.invocations) + ", " + name + "] : ")
                if (process.params != None and len(process.params) > 0):
                    params = urllib.urlencode(process.params)
                    if (process.sendMethod == "post"):
                        result = urllib2.urlopen(process.url, params)
                    else:
                        result = urllib2.urlopen(process.url + "?%s" % params)
                else:
                    result = urllib2.urlopen(process.url)
                strResult = result.read()
                # IF A HANDLER, THEN CALL IT BY PASSING THE RESULT
                if (process.resultHandler != None):
                    process.resultHandler(strResult)
                self.log(strResult + "\r\n")
            except HTTPError, e:
                self.log("[HTTP Error] : " + str(e) + "\r\n")
            except URLError, e:
                self.log("[URL Error] : " + str(e) + "\r\n")

    def log(self, msg):
        if (self.logToConsole):
            print msg
        if (self.logToFile):
            self.fileLogger.log(msg)
        self.logData += msg

if __name__ == "__main__":
    pass