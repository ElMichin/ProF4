
from cliente import Cliente #Se importa cliente para validar los clientes
from reserva import Reserva# Se importa Reserva para crear y administrar reservas

# Se importan excepciones personalizadas para controla los errores relacionados con las operaciones del sistema
from excepciones import (
    ClienteDuplicado,
    ElementoNoEncontrado,
    ErrorSoftwareFJ
)

# Se importa la clase encargada del registro de eventos
from logger_sistema import LoggerSistema


# Clase administradora del sistema Software FJ
class SistemaSoftwareFJ:

    def __init__(self):

        # Lista privada que almacena los clientes registrados
        self.__clientes = []

        # Lista privada que almacena los servicios disponibles
        self.__servicios = []

        # Lista privada que almacena las reservas realizadas
        self.__reservas = []

        # Se crea un objeto LoggerSistema para registrar las operaciones y errores
        self.logger = LoggerSistema()

        # Se registra el inicio del sistema
        self.logger.info("Sistema Software FJ iniciado.")

    # Método que permite registrar un nuevo cliente
    def registrar_cliente(self, cliente):

        #Try en caso de un error
        try:

            #Verificamos el objeto recibido
            if not isinstance(cliente, Cliente):
                raise TypeError(
                    "El objeto no es un cliente válido."
                )

            #Verifica que el cliente exista
            for existente in self.__clientes:

                #Se comparan los identificadores de los clientes
                if existente.identificador == cliente.identificador:

                    #Si el documento ya existe se genera una excepción personalizada.
                    raise ClienteDuplicado(
                        "El cliente ya está registrado."
                    )

            #Si las validaciones son exitosas se agrega el cliente a la lista interna.
            self.__clientes.append(cliente)

            #Se registra el evento en el archivo de logs.
            self.logger.info(
                f"Cliente registrado: {cliente.identificador}"
            )

            #Se retorna True indicando que el registro se realizó correctamente.
            return True

        # Se capturan las excepciones personalizadas
        # que heredan de ErrorSoftwareFJ.
        except ErrorSoftwareFJ as error:

            #Se registra el error ocurrido
            self.logger.error(
                f"Error registrando cliente: {error}"
            )

            #Se vuelve a lanzar la excepción para que la capa que llamó al método pueda manejarla
            raise

        #En caso de error se muestar mensaje
        except Exception as error:

            #Se resgistra el errro
            self.logger.exception(
                "Error inesperado registrando cliente."
            )
            raise ErrorSoftwareFJ(
                "No se pudo registrar el cliente."
            ) from error

    #Método que permite buscar un cliente utilizando su número de documento
    def buscar_cliente(self, documento):

        #Se recorre la lista interna de clientes
        for cliente in self.__clientes:

            #Se compara el identificador de cada cliente con el documento solicitado
            if cliente.identificador == documento:

                #Si se encuentra, se retorna el objeto
                return cliente

        #Si termina el recorrido sin encontrarlo genera una excepción personalizada
        raise ElementoNoEncontrado(
            "Cliente no encontrado."
        )

    #Método que devuelve los clientes registrados
    def listar_clientes(self):

        #Se retorna una copia superficial de la lista. Esto evita que se modifique directamente
        return list(self.__clientes)

    #Metodo que permite registrar un servicio
    def registrar_servicio(self, servicio):

        #Se inicia el bloque de control de excepciones.
        try:

            #Se recorren los servicios existentes para verificar que el código no esté repetido
            for existente in self.__servicios:

                #Se comparan los códigos de los servicios
                if existente.codigo == servicio.codigo:

                    #Si existe un código duplicadose genera un error
                    raise ValueError(
                        "El código del servicio ya existe."
                    )

            #Se agrega el servicio a la lista interna
            self.__servicios.append(servicio)

            #Se registra el evento en el archivo de logs
            self.logger.info(
                f"Servicio registrado: {servicio.codigo}"
            )

            #Se retorna True indicando que el registro se realizó correctamente
            return True

        #Se capturan errores durante el registro
        except Exception as error:

            #Se almacena la información del error y su traceback en el archivo de logs
            self.logger.exception(
                "Error registrando servicio."
            )

            #Se vuelve a lanzar el error para que pueda ser manejado por el programa principal
            raise

    #Método que permite buscar un servicio por su código
    def buscar_servicio(self, codigo):

        #Se recorre la lista de servicios registrados
        for servicio in self.__servicios:

            #Se verifica si el código coincide
            if servicio.codigo == codigo:

                #Si se encuentra, se retorna el servicio
                return servicio

        #Si no existe, se genera una excepción
        raise ElementoNoEncontrado(
            "Servicio no encontrado."
        )

    #Método que devuelve los servicios registrados
    def listar_servicios(self):

        #Se retorna una copia de la lista interna
        return list(self.__servicios)

    #Método que permite crear una reserva recibe cliente, servicio, duración, descuento e impuesto.
    def crear_reserva(
        self,
        cliente,
        servicio,
        duracion,
        descuento=0,
        impuesto=0
    ):

        #TRY en caso de error del programa
        try:

            # Se crea un objeto Reserva con los datos recibidos.
            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            #Se calcula el costo total de la reserva utilizando el descuento y el impuesto
            reserva.calcular_total(
                descuento,
                impuesto
            )

            #Se agrega la reserva a la lista interna
            self.__reservas.append(reserva)
            
            #Se registra la creación de la reserva
            self.logger.info(
                f"Reserva creada: {reserva.id}"
            )

            #Se retorna el objeto Reserva creado
            return reserva

        #Se capturan los errores que puedan ocurrir durante la creación o cálculo de la reserva
        except Exception as error:

            #Se registra el error con traceback
            self.logger.exception(
                "Error creando reserva."
            )

            #Se genera una excepción personalizada conservando la causa original.
            raise ErrorSoftwareFJ(
                "No se pudo crear la reserva."
            ) from error

    #Metodo que permite confirmar una reserva utilizando su identificador.
    def confirmar_reserva(self, id_reserva):

        #TRY en caso de que suceda un error
        try:

            #Se busca la reserva correspondiente
            reserva = self.buscar_reserva(id_reserva)

            #Se llama al método de confirmación del objeto
            reserva.confirmar_reserva()

            #Se registra la confirmación
            self.logger.info(
                f"Reserva confirmada: {id_reserva}"
            )

            #Se retorna True indicando éxito
            return True

        #Se capturan errores durante la confirmación
        except Exception as error:

            #Se registra el error
            self.logger.exception(
                "Error confirmando reserva."
            )

            #Se vuelve a lanzar para que el programa principal pueda manejarlo
            raise

    #Método que permite cancelar una reserva
    def cancelar_reserva(self, id_reserva):

        #Se inicia el bloque de control de errores.
        try:

            #Se busca la reserva correspondiente
            reserva = self.buscar_reserva(id_reserva)

            #Se llama al método de cancelación
            reserva.cancelar_reserva()

            #Se registra el evento de cancelación
            self.logger.info(
                f"Reserva cancelada: {id_reserva}"
            )

            #Se retorna True indicando éxito
            return True

        #Se capturan errores durante la cancelación
        except Exception as error:

            #Se registra el error en el archivo de logs
            self.logger.exception(
                "Error cancelando reserva."
            )

            #Se vuelve a lanzar la excepción
            raise

    #Método que permite buscar una reserva utilizando su identificador.
    def buscar_reserva(self, id_reserva):

        #Se recorre la lista de reservas
        for reserva in self.__reservas:

            #Se compara el identificador de la reserva
            if reserva.id == id_reserva:

                #Si se encuentra, se retorna el objeto
                return reserva

        #Si no existe, se genera una excepción
        raise ElementoNoEncontrado(
            "Reserva no encontrada."
        )

    #Método que devuelve todas las reservas
    def listar_reservas(self):

        #Se retorna una copia de la lista interna
        return list(self.__reservas)

    #Metodo que devuelve la cantidad de clientes servicios y reservas registrados
    def mostrar_resumen(self):

        #Se construye y retorna una cadena con la información general del sistema
        return (
            f"Clientes registrados: {len(self.__clientes)}\n"
            f"Servicios registrados: {len(self.__servicios)}\n"
            f"Reservas realizadas: {len(self.__reservas)}"
        )