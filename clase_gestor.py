from clase_cliente_local import cliente_local
from clase_cliente_nac import cliente_nac
from clase_nodo import Nodo

class lista:
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self

    def __next__(self):
        if self.__actual is None or self.__indice == self.__tope:
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            self.__indice += 1
            return dato

    def insertar_final(self, cliente):
        nuevo_nodo = Nodo(cliente)
        if self.__comienzo is None:
            self.__comienzo = nuevo_nodo
        else:
            actual = self.__comienzo
            while actual.getSiguiente() is not None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nuevo_nodo)
        self.__tope += 1
    
    def mostrar_clientes(self):
        actual = self.__comienzo
        while actual is not None:
            cliente = actual.getDato()
            print(cliente)
            actual = actual.getSiguiente()
    
    def buscar_cliente_nacional(self):
        aux = self.__comienzo
        while aux is not None:
            cliente = aux.getDato()
            if isinstance(cliente, cliente_nac):
                print(f"Cliente nacional: {cliente.get_nombre()}, Provincia: {cliente.get_provincia()}")
            aux = aux.getSiguiente()

    def posicion(self):
        indice = int(input("Ingrese la posición de la lista: "))
        if indice < 0 or indice >= self.__tope:
            print("Posición fuera de rango.")
            return
        actual = self.__comienzo
        contador = 0
        while actual is not None:
            if contador == indice:
                cliente = actual.getDato()
                if isinstance(cliente, cliente_local):
                    print(f"Cliente en la posición {indice}: es de tipo Cliente Local.")
                elif isinstance(cliente, cliente_nac):
                    print(f"Cliente en la posición {indice}: es de tipo Cliente Nacional.")
                return
            actual = actual.getSiguiente()
            contador += 1
        print("Posición fuera de rango.")
