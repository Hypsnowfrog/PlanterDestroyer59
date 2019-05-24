import sys
from network import *

def main():
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        connexion = Network(ip)
    elif len(sys.argv) == 3:
        ip = sys.argv[1]
        port = sys.argv[2]
        connexion = Network(ip, port)
    else:
        connexion = Network()

    connexion.send("PlanterDestroyer59 (lensleau)\n")
    numero = connexion.receive()
    print(numero)
    received = connexion.receive()
    print(received)


if __name__ == '__main__':
    main()
