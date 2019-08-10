import os
import subprocess
import pydot

pypath =os.path.dirname(os.path.abspath(__file__)) #Path relativo del archivo .py
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

    def getTamaña(self):
        return self.size
    
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

    def print_list(self):
        if self.size ==0:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            temp = self.primero
            while temp.siguiente is not self.primero:    #iterate our list printing each element-
                print(temp.valor)       #-as we go
                #print('->',end='')
                temp = temp.siguiente
                #print(temp.valor)                  #print the las element in order to avoid [1->2->3->]-
            print(temp.valor)                                   #-the last link pointing tu None (null

    def generate_graphviz(self):
        if self.primero is None:               
            print('The list is empty')     
        else:
            
            f = open(pypath+'\\nombres.dot','w')
            f.write('digraph G{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=LR;\n')
            temp = self.primero
            count = 0
            f.write('node{} -> node{};\n'.format(str(0),str(self.size-1)))
            f.write('node{} -> node{};\n'.format(str(self.size-1),str(0)))
            
            while temp.siguiente is not self.primero:
                f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.valor)))
                count+=1
                f.write('node{} -> node{};\n'.format(str(count-1),str(count)))
                f.write('node{} -> node{};\n'.format(str(count),str(count-1)))
                temp = temp.siguiente
            f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.valor)))
            f.write('}')
            f.close()
            url1 = 'nombres.dot'
            url2 = 'Rnombres.png'
            os.system('dot {} -Tpng -o {}'.format(url1,url2))



nombres = DobleCircular()
nombres.insertarFinal("Jose")
nombres.insertarFinal("Jose1")
nombres.insertarFinal("Jose2")
nombres.print_list()

nombres.generate_graphviz()