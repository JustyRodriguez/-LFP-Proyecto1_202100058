from Abstract.abstract import Expression
from math import *

class Arimetica(Expression):
    def __init__(self,left,right,tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        leftValue = ''
        rightValue = ''
        if self.tipo.operar(arbol) != None:
            leftValue = self.left.operar(arbol)
            rightValue = self.right.operar(arbol)
        elif self.right != None:
            rightValue = self.right.operar(arbol)
            
        if self.tipo.operar(arbol) == 'Suma':
            return leftValue + rightValue
        elif self.tipo.operar(arbol) == 'Resta':
            return leftValue - rightValue
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            return leftValue * rightValue
        elif self.tipo.operar(arbol) == 'Division':
            return leftValue / rightValue
        elif self.tipo.operar(arbol) == 'Mod':
            return leftValue % rightValue
        elif self.tipo.operar(arbol) == 'Potencia':
            return leftValue ** rightValue
        elif self.tipo.operar(arbol)=="Inverso":
            return 1/leftValue
        elif self.tipo.operar(arbol)=="Raiz":
            return sqrt(leftValue)
        else:
            return None
    def getFila(self):
        return super().getFila()
    def getColumna(self):
        return super().getColumna()