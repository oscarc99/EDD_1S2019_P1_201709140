import os
import subprocess
import pydot

pypath =os.path.dirname(os.path.abspath(__file__)) #Path relativo del archivo .py

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
    
    def getTamaña(self):
        return self.tamaño

    def agregar(self, nombre, puntuacion):
        punto = NodoScore(nombre,puntuacion)
        if self.tamaño==10:
            temp = self.inicio
            self.inicio=temp.siguiente
            self.fin.siguiente=punto
            self.fin=punto
        else:    
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
    
    
    def print_list(self):
        if self.tamaño ==0:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            
            
            temp = self.inicio
            if self.tamaño ==1:
                print(temp.Name+" "+  str(temp.Score) )  
            while temp is not None:    #iterate our list printing each element-
                print(temp.Name+" "+  str(temp.Score) )      
                #print('->',end='')
                temp = temp.siguiente
                #print(temp.Name+" "+ str(temp.Score))             #print the las element in order to avoid [1->2->3->]-
            #-the last link pointing tu None (null)

    def reportes_SCOREBOARD(self):
        if self.inicio is None:               
            print('The list is empty')     
        else:
            f = open(pypath+'\\registro.dot','w')
            f.write('digraph G{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=UD;\n')
            temp = self.inicio
            count = 0
            while temp.siguiente is not None:
                f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.Name)+","+str(temp.Score)))
                count+=1
                f.write('node{} -> node{};\n'.format(str(count-1),str(count)))
                
                temp = temp.siguiente
            f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.Name)+","+str(temp.Score)))
            f.write('}')
            f.close()
            url1 = 'registro.dot'
            url2 = 'Rregistro.png'
            os.system('dot {} -Tpng -o {}'.format(url1,url2))

"""
Puntos = ColaScore()
Puntos.agregar("Juan", 1)
Puntos.agregar("Juan", 2)
Puntos.agregar("Juan", 3)
Puntos.agregar("Juan", 4)
Puntos.agregar("Juan", 5)
Puntos.agregar("Juan", 6)
Puntos.agregar("Juan", 7)
Puntos.agregar("Juan", 8)
Puntos.agregar("Juan", 9)
Puntos.agregar("Juan", 10)
Puntos.agregar("Juan", 11)
#Puntos.agregar("Mario", 25)
Puntos.print_list()
Puntos.reportes_boardscore()
"""
