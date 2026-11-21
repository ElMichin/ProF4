from abc import ABC, abstractmethod #ayuda a definir las clases abastractas
from excepciones import ErrorCalculo, ServicioInvalido


class Servicio(ABC):

    def __init__(self, codigo, nombre, tarifa):

        #Se valida que el codigo exista
        if not codigo:
            raise ServicioInvalido("El código es obligatorio.")

        #Valida que el nombre no este vacio
        if not nombre or not nombre.strip():
            raise ServicioInvalido("El nombre es obligatorio.")

        #Se valida que la tarifa sea numerica siempre tenga números mayores o iguales a 0
        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise ServicioInvalido("La tarifa debe ser mayor que cero.")

        #Se guardan en la variables como privadas
        self._codigo = codigo
        self._nombre = nombre
        self._tarifa = tarifa

    #los property son encargador de ayudar en la consulta de ciertas variables dentro de las clases abastractas
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa(self):
        return self._tarifa

    #los abstractmethod son metodos abstractos 
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_disponibilidad(self, duracion):
        pass

    #ayuda con el costo total por la duracion dada por el usuario    
    def calcular_costo_base(self, duracion):

        #validador de que la duracion sea nuemerica y mayor o igual a 0     
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorCalculo("La duración debe ser mayor que cero.")

        #retorns el resultado multiplicado por la duracion
        return self.tarifa * duracion

    def __str__(self):
        return self.describir_servicio()