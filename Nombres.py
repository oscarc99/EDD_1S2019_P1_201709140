class NodoDoble():
    #Esta clase va a ser el nodo de listas
    def  __init__(self,valor):
        self.siguiente = None
        self.anterior = None
        self.valor = valor

class DobleCircular():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def estaVacia(self):
        return self.size==0
    
    def insertarFinal(self, valor):
        nuevo = NodoDoble(valor)
        if (self.estaVacia()):
            self.primero = nuevo
            self.ultimo = nuevo
            self.primero.anterior = self.ultimo
            self.primero.siguiente = self.primero
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            self.ultimo=nuevo
            self.ultimo.siguiente=self.primero
            self.primero.anterior=self.ultimo
        self.size = self.size+1
