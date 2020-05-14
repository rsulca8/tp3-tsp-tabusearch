from Vertice import Vertice
from Arista import Arista
import sys
import re
import math 
import copy


class Grafo:
    def __init__(self, M: list):
        self.__V = []
        self.__A = []
        self.__matrizDistancias = M
        self.cargarDesdeMatriz(M)
        self.__grado = 0

    def getGrado(self):
        return self.__grado

    def setA(self, A):
        self.__A = A

    def setV(self, V):
        self.__V = V



    def getA(self):
        return self.__A

    def getV(self):
        return self.__V

    #Compara entre 2. Se fija si hay aristas de A contenidas en si misma. Si hay aristas, se detiene
    def contieneA(self,A):
        sigue = True
        i = 0
        n = len(self.getA())
        while((sigue == True) and i < n):
            if(self.getA()[i].tieneOrigen(A.getOrigen()) and self.getA()[i].tieneDestino(A.getDestino())):
                sigue = False
                i=n
            i+=1
        return not(sigue)

    def getCostoArista(self, A):
        sigue = True
        i = 0
        n = len(self.getA())
        while((sigue == True) and i < n):
            if(self.getA()[i].tieneOrigen(A.getOrigen()) and self.getA()[i].tieneDestino(A.getDestino())):
                sigue = False
            i+=1
        return i-1

    def getAristaMinima(self,listaAristas):
        minimo = listaAristas[0]
        for i in listaAristas:
            if(i.getPeso() < minimo.getPeso()):
                minimo = i

        return minimo

    def cargaAristas(self):
        A=[]
        cantV = len(self.__V)
        for row in range(1,cantV):
            for col in range(1, cantV):
                arista_aux = Arista(row,col,self.__matrizDistancias[row][col])
                A.append(arista_aux)
        
        print("Aristas: \n",A)
        return A
    
    #Nose para que sirve? en q caso se lo utiliza
    def rellenarAristas(self):
        A = self.__A
        V = self.__V
        for i in V:
            for j in V:
                arista_aux = Arista(i,j,0)
                if(not(self.contieneA(arista_aux))):
                    A.append(arista_aux)

    def __str__(self):
        salida = ""
        V = self.getV()
        #Muestra la primera fila con los vertices
        if(len(self.__matrizDistancias) == len(self.getV())):
            for i in range(0,len(V)):
                salida += "     " +  str(V[i]) 

            salida = salida + "\n"
            for i in range(0,len(V)):
                salida += str(V[i]) + "    "
                for j in range(0,len(V)):
                    salida += str(self.__matrizDistancias[i][j]) + "    "
                salida = salida + "\n"
        else:
            for i in range(0,len(V)):
                salida += str(V[i]) + "    "

            salida = salida + "\n"
            for i in V:
                salida += str(i) + "    "
                for j in V:
                    indice = self.getCostoArista(Arista(i,j,0))
                    salida += str(self.getA()[indice].getPeso()) + "    "
                salida = salida + "\n"
        return salida
    
    def aristasConOrigen(self, V):
        salida = []
        for arista in self.getA():
            if((arista.tieneOrigen(V)) == True):
                salida.append(arista)

        return salida

    def aristasConDestino(self, V):
        salida = []
        for arista in self.getA():
            if((arista.tieneDestino(V)) == True):
                salida.append(arista)
        return salida
    
    #Cargar las aristas
    def cargarDesdeMatriz(self, Matriz):
        for fila in range(0,len(Matriz)):
            self.__V.append(Vertice(fila+1))    #V = [1,2,3,4,5]; V=[1,3,4] A=[(1,3)(3,4)] => sol 1->3->4->5->2
        for fila in range(0,len(Matriz)):
            for columna in range(0, len(Matriz[fila])):
                aux = Arista(self.__V[fila],self.__V[columna],(Matriz[fila][columna]))
                self.__A.append(aux)

    def getVerticeInicio(self):
        return self.__A[0].getOrigen()

    def getMatriz(self):
        return self.__matrizDistancias
    
    def setMatriz(self, M):
        self.__matrizDistancias = M

#Para que cargue desde una secuencia de vertices por ej. s1= [1,3,4,5,8,9,6,7] -> s2=[1,3,9,5,8,4,6,7]
#(1,3)(3,4)(4,5)(5,8),(8,9)(9,6)(6,7),(7,1)  
#(1,3)(3,9)(9,5)(5,8),(8,4)(4,6)(6,7),(7,1)  
#Sol vecino mas cercano
#    V = [1,2,3,4,5,6]
#    A = [(1,2)(2,3)(3,4)(4,5)(5,6)]

# g = G(M)
# s1 = g.copy()
# s1.cargarDesdeSecuenciaDeVertices([1,3,4,5,8,9,6,7])
# s2 = s1.swapVertice(4,6)
#    G = G(M)
#    return G    V



