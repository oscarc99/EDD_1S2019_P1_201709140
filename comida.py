class NodoComida():
    #Nodo para el score (pila)
    def __init__(self,posicionX, posicionY):
        self.posX = posicionX
        self.posY = posicionY
        self.siguiente = None

class PilaComida():
    #Metodo constructior pila
    def __init__(self):
        self.arriba = None
        self.tamaño=0

    def comer(self, comidaX, comidaY):
        comida = NodoComida(comidaX,comidaY)
        self.tamaño= self.tamaño+1
        if self.arriba is None:
            self.arriba=comida
        else:
            comida.siguiente=self.arriba
            self.arriba=comida

    def delete(self):
        if self.tamaño==0:
            print("Esta vacia")
        else:
            self.tamaño= self.tamaño-1
            self.temp = self.arriba
            self.arriba=self.arriba.siguiente
    
