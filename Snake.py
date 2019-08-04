class NodoSerpiente():
    #Nodo para la serpiente, (lista enlazada doble)
    def  __init__(self,posicionX, posicionY):
        self.posiX = posicionX
        self.posiY = posicionY
        self.siguient = None
        self.anterio = None

class ListaDobleSnake():
    #Motodo crear lista doble del snake
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamaño = 0

    def insertar_final(self,valorX, valorY):
        nuevo = NodoSerpiente(valorX,valorY)
        if self.tamaño==0:
            self.primero = nuevo
            self.ultimo = nuevo
            self.primero.anterio = self.ultimo
            self.primero.siguient = self.primero
        else:
           self.ultimo.siguient=nuevo
           nuevo.anterio=self.ultimo
           self.ultimo=nuevo
        self.tamaño = self.tamaño + 1
          
    def eliminarUltimo(self):
        self.tamaño=self.tamaño-1
        temporal = self.primero #aputan para ir recorriendo
        while(temporal.siguient != self.ultimo):
            temporal.siguient=None
            self.ultimo=temporal
    