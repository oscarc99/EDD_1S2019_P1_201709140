import os
import subprocess
import pydot

pypath =os.path.dirname(os.path.abspath(__file__)) #Path relativo del archivo .py

class NodoSerpiente():
    #Nodo para la serpiente, (lista enlazada doble)
    def  __init__(self,posicionX, posicionY):
        sna = posicion(posicionX, posicionY)
        self.posiX = posicionX
        self.posiY = posicionY
        self.pos=sna
        self.siguient = None
        self.anterio = None

class posicion():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class ListaDobleSnake():
    #Motodo crear lista doble del snake
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamaño = 0

    def getTamaña(self):
        return self.tamaño

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

    def print_list(self):
        if self.tamaño ==0:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            temp = self.primero
            while temp is not self.ultimo:    #iterate our list printing each element-
                print(str(temp.posiX)+","+str (temp.posiY))       #-as we go
                #print('->',end='')
                temp = temp.siguient
                #print(temp.valor)                  #print the las element in order to avoid [1->2->3->]-
            print(str(temp.posiX)+"En X "+str (temp.posiY)) 

    def generate_graphviz(self):
        if self.primero is None:               
            print('The list is empty')     
        else:
            f = open(pypath+'\\snake.dot','w')
            f.write('digraph G{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')
            temp = self.primero
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

snake = ListaDobleSnake()
snake.insertar_final(1,1)
snake.insertar_final(2,2)
snake.insertar_final(3,3)
snake.insertar_final(4,4)
snake.insertar_final(5,5)
snake.print_list()
snake.generate_graphviz()