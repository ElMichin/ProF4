from datetime import datetime
from excepciones import (
    ReservaInvalida,
    EstadoReservaInvalido,
    ErrorCalculo
)


class Reserva:

    contador = 0

    def __init__(self, cliente, servicio, duracion):

        if cliente is None:
            raise ReservaInvalida("Debe existir un cliente.")

        if servicio is None:
            raise ReservaInvalida("Debe existir un servicio.")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaInvalida("La duración debe ser positiva.")

        servicio.validar_disponibilidad(duracion)

        Reserva.contador += 1

        self.__id = f"R{Reserva.contador:03d}"
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__fecha = datetime.now()
        self.__estado = "Pendiente"
        self.__costo = 0

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def calcular_total(self, descuento=0, impuesto=0):

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                descuento,
                impuesto
            )

            return self.__costo

        except Exception as error:
            raise ErrorCalculo(
                f"Error calculando la reserva {self.__id}."
            ) from error

    def confirmar_reserva(self):

        if self.__estado != "Pendiente":
            raise EstadoReservaInvalido(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__servicio.validar_disponibilidad(self.__duracion)

        # Si se trata de alquiler de equipo, se descuenta una unidad.
        from alquiler_equipo import AlquilerEquipo

        if isinstance(self.__servicio, AlquilerEquipo):
            self.__servicio.alquilar_unidad()

        self.__estado = "Confirmada"

    def cancelar_reserva(self):

        if self.__estado == "Cancelada":
            raise EstadoReservaInvalido(
                "La reserva ya se encuentra cancelada."
            )

        if self.__estado != "Confirmada":
            raise EstadoReservaInvalido(
                "Solo se pueden cancelar reservas confirmadas."
            )

        from alquiler_equipo import AlquilerEquipo

        if isinstance(self.__servicio, AlquilerEquipo):
            self.__servicio.devolver_unidad()

        self.__estado = "Cancelada"

    def procesar_reserva(self):

        try:
            self.calcular_total()
            self.confirmar_reserva()

        except Exception as error:
            raise ReservaInvalida(
                "No fue posible procesar la reserva."
            ) from error

    def mostrar_informacion(self):

        return (
            f"Reserva: {self.id}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Fecha: {self.__fecha}\n"
            f"Estado: {self.estado}\n"
            f"Costo: ${self.costo:,.0f}"
        )

    def __str__(self):
        return self.mostrar_informacion()
