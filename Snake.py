import os
import subprocess
import pydot

#Path relativo del archivo .py
pypath =os.path.dirname(os.path.abspath(__file__)) 

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
        self.primero = None
        self.ultimo = None
        self.tamaño = 0
    #Devuelve el tamaño de la lista
    def getTamaño(self):
        return self.tamaño
    #Inserta al final de la lista
    def insertar_inicio(self,valorX, valorY):
        nuevo = NodoSerpiente(valorX,valorY)
        if self.tamaño==0:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
           self.primero.siguient=nuevo
           nuevo.anterio=self.primero
           self.primero=nuevo

        self.tamaño = self.tamaño + 1

    #Elimina el ultimo elemento de la lista      
    def eliminarUltimo(self):
        if self.tamaño==0:
            print("Lista vacia")
        else:
            temp = self.ultimo.siguient
            temp.anterio=None
            self.ultimo=temp
        self.tamaño -=1

    #Imprime los elementos de la lista
    def print_list(self):
        if self.tamaño ==0:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            temp = self.ultimo
            while temp is not None:    #iterate our list printing each element-
                print(str(temp.posiX)+","+str (temp.posiY))       #-as we go
                #print('->',end='')
                temp = temp.siguient
                #print(temp.valor)                  #print the las element in order to avoid [1->2->3->]-
            
    #Genera imagen de nodos de snake
    def reportes_snake(self):
        if self.primero is None:               
            print('The list is empty')     
        else:
            f = open(pypath+'\\snake.dot','w')
            f.write('digraph G{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')
            temp = self.ultimo
            count = 0
            while temp.siguient is not None:
                f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.posiX)+","+str(temp.posiY)))
                count+=1
                f.write('node{} -> node{};\n'.format(str(count-1),str(count)))
                f.write('node{} -> node{};\n'.format(str(count),str(count-1)))
                temp = temp.siguient
            f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.posiX)+","+str(temp.posiY)))
            f.write('}')
            f.close()
            url1 = 'snake.dot'
            url2 = 'Rsnake.png'
            os.system('dot {} -Tpng -o {}'.format(url1,url2))
            os.system(url2)

    def limpiar_snake(self):
        self.primero=None
        self.ultimo=None
        self.tamaño=0

    def mover_abajo(self):
        #Inserto al incio
        X = self.primero.posiX
        Y = self.primero.posiY+1
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
        

    def mover_arriba(self):
        #Inserto al incio
        X = self.primero.posiX
        Y = self.primero.posiY-1
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
        

    def mover_iz(self):
        #Inserto al incio
        X = self.primero.posiX-1
        Y = self.primero.posiY
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
        

    def mover_der(self):
        #Inserto al incio
        X = self.primero.posiX+1
        Y = self.primero.posiY
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
        



#Pruebas            
snake = ListaDobleSnake()
snake.insertar_inicio(11,3)
snake.insertar_inicio(12,3)
snake.insertar_inicio(13,3)
snake.insertar_inicio(14,3)
snake.insertar_inicio(15,3)
snake.mover_der()
snake.mover_arriba()
snake.print_list()
snake.reportes_snake()
