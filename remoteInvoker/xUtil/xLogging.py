__author__="ICP(ivanhalen@gmail.com)"
__date__ ="$09-may-2012 15:33:02$"

class XLogging(object):
    def __init__(self, fileName, saltoLineaAutomatico = False):
        self.__fileName = fileName
        self.__file = None
        self.__saltoLineaAutomatico = saltoLineaAutomatico

    def log(self, data):
        self.__file = open(self.__fileName, "a")
        self.__file.write(data)
        if (self.__saltoLineaAutomatico):
            self.__file.write("\r\n")
        self.__file.close()

if __name__ == "__main__":
    pass
