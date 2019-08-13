import curses 
import time
import os
import subprocess
from random import randint
import curses.textpad
from curses import textpad

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
    #Insertar final
    def insertar_final(self, valorx, valory):
        nuevo= NodoSerpiente(valorx,valory)
        if self.tamaño==0:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.anterio=nuevo
            nuevo.siguient=self.ultimo
            self.ultimo=nuevo

    #Inserta al inici de la lista
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
            x = self.ultimo.posiX
            y = self.ultimo.posiY
            
            temp = self.ultimo.siguient
            temp.anterio=None
            self.ultimo=temp
        self.tamaño -=1
        return x,y

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
        
        if X >68: 
            X= 2
        if Y >18:
            Y=2
        if X<2:
            X=68
        if Y<2:
            Y=18
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
        
    def mover_arriba(self):
        #Inserto al incio
        X = self.primero.posiX
        Y = self.primero.posiY-1
        if X >68: 
            X= 2
        if Y >18:
            Y=2
        if X<2:
            X=68
        if Y<2:
            Y=18
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
        
    def mover_iz(self):
        #Inserto al incio
        X = self.primero.posiX-1
        Y = self.primero.posiY
        if X >68: 
            X= 2
        if Y >18:
            Y=2
        if X<2:
            X=68
        if Y<2:
            Y=18
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
    
    def mover_der(self):
        #Inserto al incio
        X = self.primero.posiX+1
        Y = self.primero.posiY
        if X >68: 
            X= 2
        if Y >18:
            Y=2
        if X<2:
            X=68
        if Y<2:
            Y=18
        self.insertar_inicio(X,Y)
        #Elimino el ultimo
        self.eliminarUltimo()
     
    
    #Verifica no existe 
    def repite(self):
        firts = self.primero
        temp = self.ultimo
        while temp.siguient is not None:
            if firts.posiY == temp.posiY and firts.posiX == temp.posiX:
                return True
            temp = temp.siguient
        return False

   

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
print(str(snake.repite(2,15)))
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
                
    def graficar(self):
        if self.arriba is None:               
            print('The list is empty')   
        else:
            f= open(pypath+'\\comida.dot',"w")
            temp = self.arriba
            f.write('digraph G{\n')
            f.write('node [shape = record];\n')
            
            f.write('2[label=\"{')
            while temp.siguiente is not None:
                f.write('({},{})'.format(temp.x,temp.y))
                f.write('|')
                temp= temp.siguiente
            f.write('({},{})'.format(temp.x,temp.y))
            f.write("}\"]}")
        
            
            f.close()
            url1 = 'comida.dot'
            url2 = 'Rcomida.jpg'
            os.system('dot {} -Tjpg -o {}'.format(url1,url2))
            os.system(url2)
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
            f.write('rankdir=LR;\n')
            temp = self.inicio
            count = 0
            while temp.siguiente is not None:
                f.write('node{} [label=\"{}\"];\n'.format(str(count),str(temp.Name)+","+str(temp.Score)))
                count+=1
                f.write('node{} -> node{};\n'.format(str(count),str(count-1)))
                
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
    
    def getSig(self):
        return self.siguiente

    def getAntes(self):
        return self.anterior

    def getValor(self):
        return self.valor

class DobleCircular():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def estaVacia(self):
        return self.size==0
    
    def getInicio(self):
        return self.primero
    
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

snake = ListaDobleSnake()
snake.insertar_inicio(5,4)
snake.insertar_inicio(5,3)
snake.insertar_inicio(5,2)
"""
#Snake
snake.insertar_final(1,1)
snake.insertar_final(2,2)
snake.insertar_final(3,3)
snake.insertar_final(4,4)
snake.insertar_final(5,5)
"""
"""
#comoda
comida.comer(6,6)
comida.comer(7,7)
comida.comer(8,8)
comida.comer(9,9)
comida.comer(10,10)
comida.comer(11,11)
"""
#Names
nombres.insertarFinal("A")
nombres.insertarFinal("B")
nombres.insertarFinal("C")
nombres.insertarFinal("D")
nombres.insertarFinal("E")
#Comida suma puntos
class Food(object):
    def __init__(self, window, char='+'):
        self.x = randint(2, 18)
        self.y = randint(2, 68)
        self.char = char
        self.window = window
    
    def getXF(self):
        return self.x
    
    def getYF(self):
        return self.y
    
    def render(self):
        self.window.addstr(self.y, self.x, self.char)
        
    def reset(self):
        self.x = randint(2, 18)
        self.y = randint(2, 68)
#Comida resta puntos
class Mala(object):
    def __init__(self, window, char='*'):
        self.x = randint(3, 18)
        self.y = randint(3, 68)
        self.char = char
        self.window = window
    
    def getXF(self):
        return self.x
    
    def getYF(self):
        return self.y
    
    def render(self):
        self.window.addstr(self.y, self.x, self.char)
        
    def reset(self):
        self.x = randint(3, 15)
        self.y = randint(3, 65)

#Metodos JUEGO COMPLETO
def paint_menu(win):
    paint_title(win,' MENU  PRINCIPAL')          #paint title
    win.addstr(7,21, '1. Play')            
    win.addstr(8,21, '2. Scoreboard')       
    win.addstr(9,21, '3. User Selection')   
    win.addstr(10,21, '4. Reports')         
    win.addstr(11,21, '5. Bulk Loading')    
    win.addstr(12,21, '6. Exit')            
    win.timeout(-1)                         #wait for  an input thru t5he getch() function

def paint_carga(win):
    try:
        paint_title(win,'CARGA MASIVA') 
        win.addstr(5,18, 'Ingrese nombre del archivo')
        #win = curses.newwin(5, 60, 5, 10)
        salida = setup_input()
        win.addstr(10,18, salida)
        archivo(win,salida)
    except:
        print("No se pudo")
    
def setup_input():
    inp = curses.newwin(8,55, 0,0)
    inp.addstr(1,1, "Ingrese nombre del archivo:")
    sub = inp.subwin(3, 41, 2, 1)
    sub.border()
    sub2 = sub.subwin(1, 40, 3, 2)
    tb = curses.textpad.Textbox(sub2)
    inp.refresh()
    tb.edit()
    return tb.gather()

def archivo(win,text):
    
    try:
        f = open(text,'r')
        mensaje = f.read()
        f.close()
        

    except:
        print("No se pudo cargar archivo")    
    
        print(mensaje)
    x=mensaje.split("\n")
    try:
        for i in x:
            nombres.insertarFinal(i)
    except:
        print("No se pudo cargar archivo")    
    
        
    
def paint_users(win):
    paint_title(win,'USERS')          #paint title
    win.addstr(5,18, 'Press enter to select')
    temp = nombres.getInicio()
    key = KEY_RIGHT         #key defaulted to KEY_RIGHT
    while key != 27:                #run program while [ESC] key is not pressed
        keystroke = window.getch()  #get current key being pressed
        if keystroke is not  -1:    #key is pressed
            key = keystroke         #key direction changes

        if key == KEY_RIGHT:                #right direction
            temp= temp.getSig()             
            win.addstr(15,18, '<----- {} ----->'.format(temp.getValor()))
        elif key == KEY_LEFT:               #left direction
            temp=temp.getAntes()
            win.addstr(15,18, '<----- {} ----->'.format(temp.getValor()))
        elif key == 10:
            user = temp.getValor()
            print(user)
            return user
            
def paint_scoreboard(win):
    paint_title(win,'SCOREBOARD')          #paint title
    win.addstr(5,18, 'Name')
    win.addstr(5,28, 'Score')            
    pY=16
    
    temp = puntos.inicio
    while temp is not None:
        win.addstr(pY,18,str(temp.getName()))
        win.addstr(pY,28,str(temp.getScore()))
        pY-=1   
        
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
            try:
                snake.reportes_snake()
            except:
                print("Error en el reportes snake")
        elif(keystroke==50):#2
            try:
                comida.graficar()
            except:
                print("Error en el reportes snake")
            
            
        elif(keystroke==51):#3
            
            try:
                puntos.reportes_SCOREBOARD()
            except:
                print("Error en el reportes snake")
        elif(keystroke==52):#4
            
            try:
                nombres.reportes_user()
            except:
                print("Error en el reportes snake")
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

def play(win,pts,use):
    win.addstr(1,1, 'Jugador: '+use)
    food = Food(window,'+')
    mala = Mala(window, '*')
    com_x=food.x
    com_y=food.y
    mal_x = mala.x
    mal_y = mala.y
    window.addch(com_x,com_y,'+')
    window.addch(mal_x,mal_y,'*')
    key = KEY_RIGHT         #key defaulted to KEY_RIGHT
    
    

    time = 100
    #window.addch(pos_y,pos_x,'0')   #print initial dot
    while key != 27:                #run program while [ESC] key is not pressed
        ini = snake.ultimo
        while ini is not None:
            window.addch(ini.posiY,ini.posiX,'0')
            ini = ini.siguient
        
        

        win.addstr(1,15, 'Puntos: '+str(pts))
        window.timeout(time)         #delay of 100 milliseconds
        keystroke = window.getch()  #get current key being pressed
        if keystroke is not  -1:    #key is pressed
            key = keystroke         #key direction changes


        last = snake.ultimo
        window.addch(last.posiY,last.posiX,' ')
        ini = snake.primero
        
        if food.x==ini.posiY and food.y ==ini.posiX:
            pts +=1
            snake.insertar_final(last.posiY,last.posiX)
            comida.comer(food.x,food.y)
            food.reset()
            com_x=food.x
            com_y=food.y
            window.addch(com_x,com_y,'+')
        if pts >0 and mal_x==ini.posiY and mal_y ==ini.posiX:
                     
            pts -=1
            comida.delete()
            snake.eliminarUltimo()
            mala.reset()
            mal_x=mala.x
            mal_y=mala.y
            window.addch(mal_x,mal_y,'*')
        elif  mal_x==ini.posiY and mal_y ==ini.posiX:  
            mala.reset()
            mal_x=mala.x
            mal_y=mala.y
            window.addch(mal_x,mal_y,'*')
                
        
        if snake.repite():
            puntos.agregar(use,pts)
            snake.limpiar_snake()
            snake.insertar_inicio(5,4)
            snake.insertar_inicio(5,3)
            snake.insertar_inicio(5,2)
            key = 27
            
        

        if pts ==15: 
           time = 60
        """
        ini = snake.primero
        temp = snake.ultimo
        while temp.siguient is not None:
            if ini.posiX == temp.posiX and ini.posiY == temp.posiY:
                print("Se termino el juego ")
                break
            temp= temp.siguient
        """
        

        #window.addch(pos_y,pos_x,' ')       #erase last dot
        if key == KEY_RIGHT:                #right direction
            #pos_x = pos_x + 1               #pos_x increase
            snake.mover_der()
        elif key == KEY_LEFT:               #left direction
            #pos_x = pos_x - 1               #pos_x decrease
            snake.mover_iz()
        elif key == KEY_UP:                 #up direction
            #pos_y = pos_y - 1               #pos_y decrease
            snake.mover_arriba()
        elif key == KEY_DOWN:               #down direction
            #pos_y = pos_y + 1               #pos_y increase
            snake.mover_abajo()
            
        
        #window.addch(pos_y,pos_x,'0')       #draw new dot
        
usuario=None
pt=0         
            
stdscr = curses.initscr() #initialize console
window = curses.newwin(20,70,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen1
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        
        paint_title(window, ' PLAY ')
        if (usuario is "" or usuario is " " or usuario is None):
            usuario= paint_users(window)
        else:
            play(window, pt, usuario)
        
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
        usuario= paint_users(window)
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
        paint_carga(window)
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1


curses.endwin() #return terminal to previous state


