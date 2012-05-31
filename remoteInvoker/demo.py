__author__="ICP(ivanhalen@gmail.com)"
__date__ ="$01-may-2012 3:05:23$"

import model.invoker
# OS PARA GET PATH
import os
# SYS PARA EXIT
import sys

# UTIL : TO GET APP PATH
def get_path():
    '''Get the path to this script no matter how it's run.'''
    #Determine if the application is a py/pyw or a frozen exe.
    if hasattr(sys, 'frozen'):
        # If run from exe
        dir_path = os.path.dirname(sys.executable)
    elif '__file__' in locals():
        # If run from py
        dir_path = os.path.dirname(__file__)
    else:
        # If run from command line
        dir_path = sys.path[0]
    return dir_path

def onResult(result):
    print "onResult:" + str(result)

def onResult2(result):
    print "onResult2:" + str(result)

if __name__ == "__main__":
    print "-- INIT REMOTE INVOKER DEMO v1.5 --"
    appPath = get_path()
    invoker = model.invoker.Invoker(True, True, str(appPath + "\invoker.log"))
    """ THE FIRST PROCESS 'test' MAKES A CALL TO THE URL 'http://localhost/test.php' EVERY 5 SECONDS
    THE RESULT IS HANDLED BY THE METHOD 'onResult' """
    invoker.add_process("test", "http://localhost/test.php", 5, {"msg":"hola proceso soy test!"}, "post", onResult)
    """ THE SECOND PROCESS 'test2' IS CALLED AFTER 15 SECONDS AND MAKES A SINGLE CALL TO THE URL 'http://localhost/test.php'.
    THE RESULT IS HANDLED BY THE METHOD 'onResult2' """
    invoker.add_process("test2", "http://localhost/test.php", 15, None, "", onResult2)
    invoker.start()