from Node import *


class Tree:
    """
    Tree
    @param head cabeza del arbol
    @param num numero de nodos
    @param last_node ultimo nodo tocado
    """
    def __init__(self, head, num, last_node):
        self.head = head
        self.num = num
        self.last_node = last_node
    """
      El metodo search se encarga de buscar si el dato pasado por parametro existe en algunos de los nodos
      metidos en el arbol y además comprueba si el dato pasado por parametro es del tipo de dato seleccionado
    """
    def search(self, dato):
        self.last_node = self.head
        if self.last_node is None or type(dato) != self.head.tipo:
            return False
        while self.last_node is not None:
            if self.last_node.data == dato:
                return True
            if dato < self.last_node.data:
                self.last_node = self.last_node.left
            else:
                self.last_node = self.last_node.right
        return False
    """
    Insercion de nodos 
    """
    def insert(self, dato):
        if self.head is None:
            self.num += 1
            self.head = Node(dato, None, None, 0, None, type(dato))
            self.recolor_ingroot()
            return True
        else:
            if type(dato) != self.head.tipo:
                return False
            self.last_node = self.head
            while self.last_node is not None:
                if dato < self.last_node.data and self.last_node.left is None:
                    self.last_node.left = Node(dato, None, None, 0, self.last_node, self.head.tipo)
                    self.num += 1
                    self.fix_insertion(self.last_node.left)
                    return True
                if dato < self.last_node.data and self.last_node.left is not None:
                    self.last_node = self.last_node.left
                if dato > self.last_node.data and self.last_node.right is None:
                    self.last_node.right = Node(dato, None, None, 0, self.last_node, self.head.tipo)
                    self.num += 1
                    self.fix_insertion(self.last_node.right)
                    return True
                if dato > self.last_node.data and self.last_node.right is not None:
                    self.last_node = self.last_node.right
    """
    Recoloracion de la raiz
    """
    def recolor_ingroot(self):
        if self.head is not None and self.head.color != 1:
            self.head.color = 1
    """
    Eliminacion de nodos     
    """
    def delete(self):
        if self.last_node.right is None and self.last_node.left is None:
            if self.last_node.before is None:
                self.head = None
            else:
                if self.last_node.before.right == self.last_node:
                    self.last_node.before.right = None
                else:
                    self.last_node.before.left = None
            self.num -= 1
            self.fix_extraction(self.last_node)
            return True
        if self.last_node.right is None and self.last_node.left is not None:
            if self.last_node.before is None:
                self.head = self.last_node.left

            else:
                self.last_node.before.left = self.last_node.left
            self.num -= 1
            self.fix_extraction(self.last_node)
            return True

        if self.last_node.right is not None and self.last_node.left is None:
            if self.last_node.before is None:
                self.head = self.last_node.right
            else:
                self.last_node.before.right = self.last_node.right
            self.num -= 1
            self.fix_extraction(self.last_node)
            return True
        if self.last_node.right is not None and self.last_node.left is not None:
            if self.last_node.before is None:
                sucesor = self.last_node.right
                sucesor2 = self.last_node.left
                self.head = sucesor
                self.head.left = sucesor2
            else:
                dato = self.last_node.data
                camino = self.in_order()
                for i in range(0, len(camino)):
                    if camino[i] == dato:
                        self.last_node.before = camino[i+1]
            self.num -= 1
            self.fix_extraction(self.last_node)
            return True
        return False
    """
    Este caso es si no existiera más que 1 nodo que es el raiz
    """
    def delete_root(self):
        if self.last_node.before is None:
            self.head = None
            self.num -= 1
            return True
    """
    La función fix_insertion restablece las propiedades del árbol Rojo-Negro tras una inserción
    """
    def fix_insertion(self, node):
        while node != self.head and node.before.color == 0:  # Mientras el nodo no sea la raíz y su padre sea rojo
            if node.before == node.before.before.right:  # Si el padre es el hijo derecho del abuelo
                uncle = node.before.before.left  # El hijo izquierdo del abuelo es el tío
                if uncle is not None and uncle.color == 0:  # Si el tío es rojo
                    uncle.color = 1  # Establecer ambos nodos hijos del abuelo como negros
                    node.before.color = 1
                    node.before.before.color = 0  # Establecer el nodo abuelo como rojo
                    node = node.before.before
                else:
                    if node == node.before.left:  # Si el nodo es el hijo izquierdo de su padre
                        node = node.before
                        self.rotate_right(node)  # Realizar una rotación a la derecha sobre el nodo
                    node.before.color = 1
                    node.before.before.color = 0
                    self.rotate_left(node.before.before)  # Realizar una rotación a la derecha sobre el abuelo
            else:  # Si el padre es el hijo izquierdo del abuelo
                uncle = node.before.before.right  # El hijo derecho del abuelo es el tío
                if uncle is not None and uncle.color == 0:  # Si el tío es rojo
                    uncle.color = 1  # Establecer ambos nodos hijos del abuelo como negros
                    node.before.color = 1
                    node.before.before.color = 0  # Establecer el nodo abuelo como rojo
                    node = node.before.before
                else:
                    if node == node.before.right:  # Si el nodo es el hijo derecho de su padre
                        node = node.before
                        self.rotate_left(node)  # Realizar una rotación a la izquierda sobre el nodo
                    node.before.color = 1
                    node.before.before.color = 0
                    self.rotate_right(node.before.before)  # Realizar una rotación a la izquierda sobre el abuelo
        self.recolor_ingroot()
    """
    La función fix_extraction reestablece las propiedades del árbol Rojo-Negro tras una extracción
    """
    def fix_extraction(self, node):
        while node != self.head and node.color == 1:  # Mientras el nodo no sea la raíz y sea de color negro
            if node.before is None:
                break
            if node == node.before.left:  # Si el nodo es el hijo izquierdo de su padre
                hermano = node.before.right  # El hijo derecho es su hermano
                if hermano is not None and hermano.color == 0:  # Si su hermano es rojo
                    hermano.color = 1  # Establecer su color como negro
                    node.before.color = 0  # Establecer al padre como rojo
                    self.rotate_left(node.before)  # Realizar una rotación a la izquierda sobre el padre
                    hermano = node.before.right
                if hermano is None:
                    break
                # Si ambos hijos del hermano son negros
                if (hermano.left is None or hermano.left.color == 1) and \
                        (hermano.right is None or hermano.right.color == 1):
                    hermano.color = 0  # Establecer al hermano como rojo
                    node = node.before
                else:
                    if hermano.right is None or hermano.right.color == 1:  # Si el hijo derecho del hermano es negro
                        if hermano.left is not None:
                            hermano.left.color = 1  # Establecer al hijo izquierdo como negro
                        hermano.color = 0  # Establecer al hermano como rojo
                        self.rotate_right(hermano)  # Realizar rotación a la derecha sobre el hermano
                        hermano = node.before.right
                    hermano.color = node.before.color
                    node.before.color = 1  # Establecer al padre como negro
                    if hermano.right is not None:
                        hermano.right.color = 1
                    self.rotate_left(node.before)  # Realizar rotación a la izquierda sobre el padre
                    node = self.head
            else:  # Si el nodo es el hijo derecho de su padre
                hermano = node.before.left  # El hijo izquierdo es su hermano
                if hermano is not None and hermano.color == 0:  # Si su hermano es rojo
                    hermano.color = 1  # Establecer su color como negro
                    node.before.color = 0  # Establecer al padre como rojo
                    self.rotate_right(node.before)  # Realizar una rotación a la derecha sobre el padre
                    hermano = node.before.left
                if hermano is None:
                    break
                # Si ambos hijos del hermano son negros
                if (hermano.right is None or hermano.right.color == 1) and \
                        (hermano.left is None or hermano.left.color == 1):
                    hermano.color = 0  # Establecer al hermano como rojo
                    node = node.before
                else:
                    if hermano.left is None or hermano.left.color == 1:  # Si el hijo izquierdo del hermano es negro
                        if hermano.right is not None:
                            hermano.right.color = 1  # Establecer al hijo derecho como negro
                        hermano.color = 0  # Establecer al hermano como rojo
                        self.rotate_left(hermano)  # Realizar rotación a la izquierda sobre el hermano
                        hermano = node.before.left
                    hermano.color = node.before.color
                    node.before.color = 1  # Establecer al padre como negro
                    if hermano.left is not None:
                        hermano.left.color = 1
                    self.rotate_right(node.before)  # Realizar rotación a la derecha sobre el padre
                    node = self.head
        self.recolor_ingroot()
    """
    Rotación hacia la izquierda
    """
    def rotate_left(self, node):
        pivot = node.right
        node.right = pivot.left
        if pivot.left is not None:
            pivot.left.before = node
        pivot.before = node.before
        if node.before is None:
            self.head = pivot
        elif node == node.before.left:
            node.before.left = pivot
        else:
            node.before.right = pivot
        pivot.left = node
        node.before = pivot
    """
    Rotación hacia la derecha
    """
    def rotate_right(self, node):
        pivot = node.left
        node.left = pivot.right
        if pivot.right is not None:
            pivot.right.before = node
        pivot.before = node.before
        if node.before is None:
            self.head = pivot
        elif node == node.before.right:
            node.before.right = pivot
        else:
            node.before.left = pivot
        pivot.right = node
        node.before = pivot
    """
    La funcion num_nodes devuelve el numero de nodos del arbol
    """
    def num_nodes(self):
        return self.num
    """
    El recorrido inorder del arbol
    """
    def in_order(self):
        pila = []
        resultado = []
        nodo = self.head
        while len(pila) != 0 or nodo is not None:
            if nodo is not None:
                pila.append(nodo)
                nodo = nodo.left
            else:
                nodo = pila.pop()
                resultado.append(nodo)
                nodo = nodo.right
        return resultado
