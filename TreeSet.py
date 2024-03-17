import copy


class TreeSet:
    """
    TreeSet
    :param arbol rojo-negro
    """

    def __init__(self, arbol):
        self.arbol = arbol

    """
    insercion de nodo
    """

    def add(self, dato):
        if self.arbol.search(dato) is True:
            return False
        else:
            return True if self.arbol.insert(dato) else False

    """
    El metodo addAll se encarga de añadir un conjunto de datos introducidos en un conjunto
    en el arbol rojo-negro
    """

    def add_all(self, dataset):
        for i in range(0, len(dataset)):
            if self.add(dataset[i]) is not True:
                return False
        return True

    """
    Halla el valor mayor o igual al dato pasado
    :param dato
    """

    def ceiling(self, data):
        camino = self.arbol.in_order()
        resultado = None
        for i in range(0, len(camino)):
            if camino[i].data >= data:
                resultado = camino[i].data
                break
        return resultado

    """
    Halla el valor mayor al dato pasado
    :param dato
    """

    def higher(self, data):
        camino = self.arbol.in_order()
        resultado = None
        for i in range(0, len(camino)):
            if camino[i].data > data:
                resultado = camino[i].data
                break
        return resultado

    """
    Halla el valor menor al dato pasado
    :param dato 
    """

    def floor(self, data):
        camino = self.arbol.in_order()
        resultado = None
        for i in range(0, len(camino)):
            if camino[i].data <= data:
                resultado = camino[i]
        return resultado

    """
    Halla el valor más pequeño del conjunto si existe sino existe None
    """

    def first(self):
        minimo = self.arbol.head
        dato = None
        while minimo is not None:
            if minimo == self.arbol.head:
                dato = self.arbol.head
            if minimo.data < dato.data:
                dato = minimo
            minimo = minimo.left

        return dato

    """
      Halla el valor más grande del conjunto si existe sino existe None
      """

    def last(self):
        minimo = self.arbol.head
        dato = None
        while minimo is not None:
            if minimo == self.arbol.head:
                dato = self.arbol.head
            if minimo.data > dato.data:
                dato = minimo
            minimo = minimo.right
        return dato

    """
    El metodo clear inicializa el arbol desde el principio dejandolo 
    como el del inicio
    """

    def clear(self):
        if self.arbol.num > 0:
            self.arbol.head = None
            self.arbol.num = 0
            self.arbol.last_node = None

    """
    Clona el TreeSet
    """

    def clone(self):
        return copy.deepcopy(TreeSet(self.arbol))

    """
    Comprueba si existe o no
    :param : data
    """

    def contains(self, data):
        return self.arbol.search(data)

    """
    Comprueba si el TreeSet esta vacio o no
    """

    def is_empty(self):
        return True if self.size() == 0 else False

    """
    Eliminar dato de la estructura
    :param data
    """

    def remove(self, data):
        if self.arbol.search(data) is True:
            if self.arbol.delete() is True:
                return True
        else:
            return False
    """
    Devuelve el numero de nodos
    """
    def size(self):
        return self.arbol.num_nodes()
    """
    Elimina el elemento mas pequeño del conjunto y luego lo devuelve
    """
    def poll_first(self):
        return self.first().data if self.remove(self.first().data) is True else None
    """
    Elimina el elemento mas grande del conjunto y luego lo devuelve
    """
    def poll_last(self):
        return self.last().data if self.remove(self.last().data) is True else None
