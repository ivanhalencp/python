__author__="ICP(ivanhalen@gmail.com)"
__date__ ="$17-may-2012 12:04:32$"

class Process():
    def __init__(self, name, url, time, params = None, sendMethod = "post", resultHandler = None):
        self.name = name
        self.url = url
        self.time = time
        self.params = params
        self.sendMethod = sendMethod
        self.invocations = 0
        self.timer = None
        self.resultHandler = resultHandler

    def add_param(self, name, value):
        if (self.params == None):
            self.params = {}
        self.params[name] = value

if __name__ == "__main__":
    pass