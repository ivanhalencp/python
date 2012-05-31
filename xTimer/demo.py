import xTimer

__author__="ICP(ivanhalen@gmail.com)"
__date__ ="$02-may-2012 23:41:48$"

def saludar():
    print "Hola !!"

def terminar(texto):
    global xT1
    print texto
    xT1.terminate()

if __name__ == "__main__":
    # CADA 2 SEGUNDOS SE EJECUTA INFINITAMENTE
    xT1 = xTimer.XTimer(2, saludar)
    xT1.start()
    # CADA 10 SEGUNDOS SE EJECUTA SOLO 1 VEZ
    xT2 = xTimer.XTimer(10, terminar, "Adios mundo cruel !!", 1)
    xT2.start()