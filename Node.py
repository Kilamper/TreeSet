class Node:
    """
    :param data dato del nodo
    :param left hijo izquierdo del nodo
    :param right hijo derecho del nodo
    :param color  color que le corresponde al nodo 0 si es rojo e 1 si es negro
    :param before almacena el before
    """
    def __init__(self, data, left, right, color, before, tipo):
        self.__data = data
        self.__left = left
        self.__right = right
        self.__color = color
        self.__before = before
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, dato):
        self.__data = dato

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        self.__right = node

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, colors):
        self.__color = colors

    @property
    def before(self):
        return self.__before

    @before.setter
    def before(self, before):
        self.__before = before
