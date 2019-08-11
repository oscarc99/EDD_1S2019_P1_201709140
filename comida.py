import os
import subprocess
import pydot

pypath =os.path.dirname(os.path.abspath(__file__)) #Path relativo del archivo .py

class NodoComida():
    #Nodo para el score (pila)
    def __init__(self,x,y):
        
        self.x=x
        self.y=y
        
        self.siguiente = None

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
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

    def getTamaño(self):
        return self.tamaño

    def delete(self):
        if self.tamaño==0:
            print("Esta vacia")
        else:
            self.tamaño= self.tamaño-1
            self.temp = self.arriba
            self.arriba=self.arriba.siguiente
    
    def print_list(self):
        if self.tamaño ==0:               #verify if our LinkedList is empty
            print('The list is empty')      #print a warning
        else:
            temp = self.arriba
            while temp.siguiente is not None:    #iterate our list printing each element-
                print(str(temp.x)+","+str (temp.y))       #-as we go
                #print('->',end='')
                temp = temp.siguiente
                #print(temp.valor)                  #print the las element in order to avoid [1->2->3->]-
            print(str(temp.x)+"En X "+str (temp.y)) 
    
    def reportes_comida(self):
        if self.arriba is None:               
            print('The list is empty')     
        else:
            f = open(pypath+'\\puntos.dot','w')
            f.write('digraph G{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=UD;\n')
            temp = self.arriba
            count = 0
            while temp.siguiente is not None:
                f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.x)+","+str(temp.y)))
                count+=1
                f.write('node{} -> node{};\n'.format(str(count-1),str(count)))
                
                temp = temp.siguiente
            f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.x)+","+str(temp.y)))
            f.write('}')
            f.close()
            url1 = 'puntos.dot'
            url2 = 'Rpuntos.png'
            os.system('dot {} -Tpng -o {}'.format(url1,url2))

"""
puntos = PilaComida()
puntos.comer(1,1)
puntos.comer(2,2)
puntos.comer(3,3)
puntos.comer(4,4)
puntos.comer(5,5)
puntos.print_list()
puntos.reportes_comida()
"""