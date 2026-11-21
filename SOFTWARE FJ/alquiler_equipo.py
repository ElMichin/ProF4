from servicio import Servicio
from excepciones import ServicioNoDisponible, ErrorCalculo

#Alquiler de equipos tambien esta heredando de Servicio
class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, tarifa, cantidad):

        super().__init__(codigo, nombre, tarifa)

        #Se verifica que la cantidad sea un entero
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        #Se almacena de equipos disponibles
        self.__cantidad = cantidad

    @property   
    def cantidad(self):
        return self.__cantidad

    #Metodo que verifca la disponibilidad del equipo
    def validar_disponibilidad(self, duracion):

        #Verificador de unidades disponibles
        if self.__cantidad <= 0:
            raise ServicioNoDisponible(
                f"No hay unidades disponibles de {self.nombre}."
            )

        #Se verifica que la duracio sea positiva 
        if duracion <= 0:
            raise ErrorCalculo("La duración debe ser mayor que cero.")

        #En caso de que no se prsenten errores, se confirma que el equipo esta disponible
        return True

    #Calcular el costo de los alquileres de equipo
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        #Try para que no se rompa el codigo en caso de error
        try:
            self.validar_disponibilidad(duracion)

            #Se calcula el costo base
            subtotal = self.calcular_costo_base(duracion)

            #Se verifica que el descuento sea valido
            if not 0 <= descuento <= 1:
                raise ErrorCalculo("Descuento inválido.")

            #Se verifica que el impuesto sea valido
            if not 0 <= impuesto <= 1:
                raise ErrorCalculo("Impuesto inválido.")

            #Se aplica el descuento al subtotal
            subtotal -= subtotal * descuento

            #Se aplica el impuesto al subtotal descontando
            subtotal += subtotal * impuesto

            #Se retorna el costo final redondeado
            return round(subtotal, 2)

        #En caso de error se mostrara un mensaje
        except ValueError as error:
            raise ErrorCalculo(
                "No fue posible calcular el alquiler del equipo."
            ) from error

    #Describe las caracteristicas del equipo
    def describir_servicio(self):
        
        return (
            f"Equipo: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa:,.0f} | "
            f"Cantidad disponible: {self.cantidad}"
        )


    #Disminiuye la cantidad disponible cuando se realiza el alquiler de una unidad
    def alquilar_unidad(self):

        self.validar_disponibilidad(1)
        self.__cantidad -= 1

    #Aumenta la cantidad disponible cuando se devuele un equipo alquilado
    def devolver_unidad(self):

        self.__cantidad += 1