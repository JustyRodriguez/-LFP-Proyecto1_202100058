from abc import ABC, abstractmethod

class Expression(ABC):
    
    def __init__(self, fila, columna) -> None:
        self.fila = fila
        self.columna = columna
        
    @abstractmethod
    def operar(self,arbol):
        pass
    
    @abstractmethod
    def getFila(self):
        pass
    @abstractmethod
    def getColumna(self):
        pass