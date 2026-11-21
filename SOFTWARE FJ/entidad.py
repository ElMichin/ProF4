from abc import ABC, abstractmethod
#La libreria que se esta importando es para las clases abstractas

class Entidad(ABC):

    #Verificacion que el idetificador no este vacio, en caso tal de que si se va generar un error
    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        #Se almacena como atributo privado
        self.__identificador = identificador

    @property
    def identificador(self):
        return self.__identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass