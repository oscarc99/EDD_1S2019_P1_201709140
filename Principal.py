class NodoSerpiente():
    #Nodo para la serpiente
    def  __init__(self,posicionX, posicionY):
        self.posX = posicionX
        self.posY = posicionY
        self.siguiente = None
        self.anterior = None
