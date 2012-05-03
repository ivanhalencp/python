import xTimer

__author__="IvoX(ivanhalen@gmail.com)"
__date__ ="$02-may-2012 23:41:48$"

def saludar():
    print "Hola !!"

def terminar():
    global xT1
    print "Chau !!"
    xT1.terminate()

if __name__ == "__main__":
    # CADA 2 SEGUNDOS SE EJECUTA INFINITAMENTE
    xT1 = xTimer.XTimer(2, saludar)
    xT1.start()
    # CADA 10 SEGUNDOS SE EJECUTA SOLO 1 VEZ
    xT2 = xTimer.XTimer(10, terminar, 1)
    xT2.start()