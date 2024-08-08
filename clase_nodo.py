class Nodo:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__cliente