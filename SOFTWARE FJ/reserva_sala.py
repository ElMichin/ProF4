from servicio import Servicio
from excepciones import ServicioNoDisponible, ErrorCalculo

#ReservaSala esta heredando de Serivicio
class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, tarifa, capacidad, disponible=True):

        super().__init__(codigo, nombre, tarifa)


        #Validamos la capacidad que sea mayor de 0 y que sea un número entero
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")

        #Se almacenan los atributos como variables privadas
        self.__capacidad = capacidad
        self.__disponible = disponible

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def disponible(self):
        return self.__disponible

    #Valida la disposicion 
    def validar_disponibilidad(self, duracion):

        #En caso tal que la sala no este disponible se va mostrar
        if not self.__disponible:
            raise ServicioNoDisponible("La sala no está disponible.")

        #Valida que la duracion sea mayor a 0
        if duracion <= 0:
            raise ErrorCalculo("La duración debe ser positiva.")

        return True

    #Metodo para calcular el costo de la sala
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        #Try para que en caso de error el ssitema no deje de funcionar    
        try:

            #Verificamos la sala si esta disponible
            self.validar_disponibilidad(duracion)

            #Se realiza el calculo del costo base
            subtotal = self.calcular_costo_base(duracion)

            #Se verifica el descuento de 0% y 100%
            if not 0 <= descuento <= 1:
                raise ErrorCalculo("El descuento debe estar entre 0 y 1.")

            #Validamos si tenemos un impuesto dentro del rango
            if not 0 <= impuesto <= 1:
                raise ErrorCalculo("El impuesto debe estar entre 0 y 1.")

            #Se calcula el valor del dsecuento y se resata al costo base
            subtotal -= subtotal * descuento

            #Se calcula el impuesto sobre el subtotal despues de aplicar el descuento.
            subtotal += subtotal * impuesto

            #Se retorna ele total redondeando     
            return round(subtotal, 2)

        #En caso de error mostrara un mensaje
        except ValueError as error:
            raise ErrorCalculo("Error calculando el costo de la sala.") from error

    #Muestra la descripcion donde especifica la sala
    def describir_servicio(self):

        #Se crea una cadena con los datos de la sala
        return (
            f"Sala: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa:,.0f} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Disponible: {self.disponible}"
        )

    #Cambia la disponibilida de la sala 
    def cambiar_disponibilidad(self, estado):

        #Se verifica que el estado en el que esta sea verdadero o falso
        if not isinstance(estado, bool):
            raise ValueError("La disponibilidad debe ser True o False.")

        #Se hace la actualizacion
        self.__disponible = estado
        