import curses 
import time
import os
import subprocess
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
#Path relativo
pypath =os.path.dirname(os.path.abspath(__file__)) 
#Metodos LISTA ENLAZADA DOBLE (SNAKE)
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
    #Elimina el ultimo elemento de la lista      
    def eliminarUltimo(self):
        self.tamaño=self.tamaño-1
        temporal = self.primero #aputan para ir recorriendo
        while(temporal.siguient != self.ultimo):
            temporal.siguient=None
            self.ultimo=temporal
    #Limpia la lista de la serpiente
    def limpiar_snake(self):
        self.primero=None
        self.ultimo=None
        self.tamaño=0
    #Imprime los elementos de la lista
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
            print(str(temp.posiX)+","+str (temp.posiY)) 
    #Genera imagen de nodos de snake
    def reportes_snake(self):
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
            os.system('Rsnake.png')

#Pruebas  snake
"""
print("PRUEBAS SNAKE")          
snake = ListaDobleSnake()
snake.insertar_final(1,1)
snake.insertar_final(2,2)
snake.insertar_final(3,3)
snake.insertar_final(4,4)
snake.insertar_final(5,5)
snake.print_list()
snake.reportes_snake()
"""
#Metodos pila score(puntos en juego/comida) 
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
    #Limpia la comida de un juego
    def limpiar_comida(self):
        self.arriba=None
        self.tamaño=0
    #Guarda la comida 
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
            os.system('Rpuntos.png')            
 
"""
print("PRUEBAS PILA COMIDA")
puntos = PilaComida()
puntos.comer(11,1)
puntos.comer(22,2)
puntos.comer(33,3)
puntos.comer(44,4)
puntos.comer(55,5)
puntos.print_list()
puntos.reportes_comida()
"""
#Meotodos SCOREBOARD (fila/cola)
class NodoScore():
    #Nodo para puntajes (Fila)
    def __init__(self,Name, Score):
        self.Name = Name
        self.Score = Score
        self.siguiente = None
    
    def getSig(self):
        return self.siguiente

    def getName(self):
        return self.Name

    def getScore(self):
        return self.Score

        
class ColaScore():
    #Metodo constructior pila
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño=0
    
    def getInicio(self):
        return self.inicio

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
            os.system('Rregistro.png')



"""
Puntos.agregar("Juan", 10)
Puntos.agregar("Juan", 11)
#Puntos.agregar("Mario", 25)
Puntos.print_list()
Puntos.reportes_boardscore()
"""
#Metodos registro nombres (circular doble)
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

    def reportes_user(self):
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
            os.system('Rnombres.png')
"""
nombres = DobleCircular()
nombres.insertarFinal("Jose")
nombres.insertarFinal("Jose1")
nombres.insertarFinal("Jose2")
nombres.print_list()
nombres.reportes_user()
"""
#Variables utilizadas en el juego
user=None
pts=None
#Variables de las lista
nombres = DobleCircular()
puntos = ColaScore()
comida = PilaComida()
snake = ListaDobleSnake()
#Ingresos de prueba
#Scoreboard
puntos.agregar("Juan", 1)
puntos.agregar("Juan", 2)
puntos.agregar("Juan", 3)
puntos.agregar("Juan", 4)
puntos.agregar("Juan", 5)
puntos.agregar("Juan", 6)
puntos.agregar("Juan", 7)
puntos.agregar("Juan", 8)
puntos.agregar("Juan", 9)
puntos.agregar("Juan", 10)
#Snake
snake.insertar_final(1,1)
snake.insertar_final(2,2)
snake.insertar_final(3,3)
snake.insertar_final(4,4)
snake.insertar_final(5,5)
#comoda
comida.comer(6,6)
comida.comer(7,7)
comida.comer(8,8)
comida.comer(9,9)
comida.comer(10,10)
comida.comer(11,11)
#Names
nombres.insertarFinal("Andres")
nombres.insertarFinal("B")
nombres.insertarFinal("C")
nombres.insertarFinal("D")
nombres.insertarFinal("E")
#Metodos JUEGO COMPLETO
def paint_menu(win):
    paint_title(win,' MENU  PRINCIPAL')          #paint title
    win.addstr(7,21, '1. Play')            
    win.addstr(8,21, '2. Scoreboard')       
    win.addstr(9,21, '3. User Selection')   
    win.addstr(10,21, '4. Reports')         
    win.addstr(11,21, '5. Bulk Loading')    
    win.addstr(12,21, '6. Exit')            
    win.timeout(-1)                         #wait for  an input thru the getch() function

def paint_scoreboard(win):
    paint_title(win,'SCOREBOARD')          #paint title
    win.addstr(5,18, 'Name')
    win.addstr(5,28, 'Score')            
    pY=7
    
    temp = puntos.getInicio()
    while temp is not None:
        win.addstr(pY,18,str(temp.getName()))
        win.addstr(pY,28,str(temp.getScore()))
        pY+=1   
        
        temp = temp.getSig()
    
    win.timeout(-1)  

def paint_report(win):
    paint_title(win,' REPORTS')          #paint title
    win.addstr(8,21, '1. SNAKE REPORT')            
    win.addstr(9,21, '2. SCORE REPORT') 
    win.addstr(10,21,'3. SCOREBOARD REPORT') 
    win.addstr(11,21,'4. USERS REPORT') 
    menu_report(window)
    
    
def menu_report(win):
    keystroke = -1
    while(keystroke==-1):
        keystroke = window.getch()  #get current key being pressed
        if(keystroke==49): #1
            snake.reportes_snake()
            
        elif(keystroke==50):#2
            comida.reportes_comida()
            
        elif(keystroke==51):#3
            puntos.reportes_SCOREBOARD()
            
        elif(keystroke==52):#4
            nombres.reportes_user()
            
        else:

            pass
    
    


def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()


stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen1
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        paint_title(window, ' PLAY ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')
        paint_scoreboard(window)
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' USER SELECTION ')
        
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        paint_report(window)
        
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' BULK LOADING ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state
