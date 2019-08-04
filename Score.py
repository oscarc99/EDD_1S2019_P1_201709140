class NodoScore():
    #Nodo para puntajes (Fila)
    def __init__(self,Name, Score):
        self.Name = Name
        self.Score = Score
        self.siguiente = None
        
class ColaScore():
    #Metodo constructior pila
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño=0

    def agregar(self, nombre, puntuacion):
        punto = NodoScore(nombre,puntuacion)
        self.tamaño= self.tamaño+1
        if self.inicio is None:
            self.inicio=punto
            self.fin=punto
        else:
            self.fin.siguiente=punto
            self.fin=punto
            
       
    def eliminar(self):
        if self.tamaño==0:
            print("Esta vacia")
        else:
            temp = self.inicio
            self.inicio=temp.siguiente
            self.tamaño = self.tamaño-1