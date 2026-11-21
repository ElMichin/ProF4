from servicio import Servicio
from excepciones import ErrorCalculo

#Asesoria hereda de Servicio
class Asesoria(Servicio):

    def __init__(self, codigo, nombre, tarifa, especialidad, asesor):

        super().__init__(codigo, nombre, tarifa)

        #Valida si la especialidad ya esta definida
        if not especialidad:
            raise ValueError("La especialidad es obligatoria.")

        #Valida que exista el nombre del asesor
        if not asesor:
            raise ValueError("El asesor es obligatorio.")

        #Se almacena los atributos como privados
        self.__especialidad = especialidad
        self.__asesor = asesor

    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def asesor(self):
        return self.__asesor

    #Metodo que valida di la sesoria puede realizarse
    def validar_disponibilidad(self, duracion):

        #Se verifica que la duracion sea positiva
        if duracion <= 0:
            raise ErrorCalculo("La duración debe ser positiva.")

        return True

    #Si no hay errores, se indica que la sesoria esta disponible
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        #Try en caso de erro
        try:

            #Se verifica que la duracion sea valida
            self.validar_disponibilidad(duracion)

            #Se calcula el costo base de la asesoria
            subtotal = self.calcular_costo_base(duracion)

            #Se verifica que el ddescuento este entre 0% A 100%
            if not 0 <= descuento <= 1:
                raise ErrorCalculo("Descuento inválido.")

            #Se valida el porcentaje del impuesto
            if not 0 <= impuesto <= 1:
                raise ErrorCalculo("Impuesto inválido.")

            #Se aplica el descuento al costo base
            subtotal -= subtotal * descuento
            #SSe aplica el impuesto al valor descontado
            subtotal += subtotal * impuesto

            #Se retorna el resultado redondeado 
            return round(subtotal, 2)

        #En caso de error se va mostrar un mensaj
        except ValueError as error:
            raise ErrorCalculo(
                "Error al calcular el costo de la asesoría."
            ) from error

    #Muestra la informacion especifica de la asesoria
    def describir_servicio(self):

        return (
            f"Asesoría: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Asesor: {self.asesor} | "
            f"Tarifa por hora: ${self.tarifa:,.0f}"
        )