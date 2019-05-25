import sys

import re

from PlanterDestroyer59.decode import decode, process, convert, convertStringInt, convertPos
from PlanterDestroyer59.network import Network
from PlanterDestroyer59.bonus import IA




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
    received = received.split("=")[1]
    #print(process(decode(re.search("([0-9]+([:\|]))+", received).group(0))))
    print(received)
    received = convertStringInt(received)
    ia = IA(process(received))
    while received[0] != "8":
        received = connexion.receive()
        if received[0] == "1" and received[1] == "0":
            pos = convertPos(ia.nextAction())
            print("pos")
            print(pos)
            conversionPos = convert(pos)
            print("convertpos")
            print(conversionPos)
            ia.addParcelJouer(conversionPos)
            connexion.send(pos)
        elif received[0] == "2" and received[1] == "0":
            ia.addParcelJouer(convert(received[-3]+received[-2]+received[-1]))


if __name__ == '__main__':
    main()
