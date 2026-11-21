from sistema import SistemaSoftwareFJ# Se importa la clase administradora del sistema.
# Se importan las clases necesarias para crear objetos.
from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria import Asesoria

# Se importa la excepción general del sistema.
from excepciones import ErrorSoftwareFJ


# Se crea una función encargada de ejecutar pruebas.
def ejecutar_prueba(nombre, operacion):

    #Para mayor orden se separan
    print(f"\n{'=' * 50}")

    #Se muestra el nombre de la prueba que se ejecutará
    print(f"PRUEBA: {nombre}")

    #Se imprime otro separado
    print("=" * 50)

    #Try por si hay algun error
    try:

        #Se ejecuta la operación recibida como parámetro operacion es una función que se envía a ejecutar
        resultado = operacion()

    #En caso de error se muestra el mesnaje y se captura que error sucedio
    except Exception as error:

        print(f"ERROR CONTROLADO: {error}")

        sistema.logger.error(
            f"Prueba fallida [{nombre}]: {error}"
        )

    #El bloque else se ejecuta únicamente si no se produjo ninguna excepción en el try
    else:

        #Se informa que la operación fue exitosa
        print("OPERACIÓN EXITOSA.")

        #Si la operación devuelve un resultado este se imprime en la consola
        if resultado is not None:
            print(resultado)

    finally:

        #Mensaje de terminado
        print("Prueba finalizada.")

        #Se imprime un separador para organizar los resultados de la siguiente prueba
        print("-" * 50)

#Se crea el objeto principal que administrará clientes, servicios y reservas
sistema = SistemaSoftwareFJ()

#--------PRUEBA 1: REGISTRO DE CLIENTE VÁLIDO--------
#Función que crea y registra un cliente correctamente
def prueba_cliente_valido():

    #Se crea un objeto Cliente con datos validos
    cliente = Cliente(
        "1001",
        "Juan Perez",
        "juan@gmail.com",
        "3101234567"
    )

    #Se registra el cliente en el sistema
    sistema.registrar_cliente(cliente)

    #Se retorna la información del cliente para mostrarla en la consola
    return cliente.mostrar_informacion()


#Se ejecuta la prueba utilizando la función general
ejecutar_prueba(
    "Registro de cliente válido",
    prueba_cliente_valido
)
#--------PRUEBA 2: REGISTRO DE CLIENTE INVÁLIDO--------
#Función que intenta registrar un cliente con un correo electrónico incorrecto
def prueba_cliente_invalido():

    #Se intenta crear el objeto Cliente. El correo no cumple con el formato requerido, por lo que se generará una excepción
    cliente = Cliente(
        "1002",
        "Maria Lopez",
        "correo_invalido",
        "3101234567"
    )

    #Esta instrucción solo se ejecutaría si el constructor no generara una excepción
    sistema.registrar_cliente(cliente)


#Se ejecuta la prueba
ejecutar_prueba(
    "Registro de cliente con correo inválido",
    prueba_cliente_invalido
)

#--------PRUEBA 3: REGISTRO DE CLIENTE DUPLICADO--------
#Función que intenta registrar un cliente con un documento que ya existe
def prueba_cliente_duplicado():

    #Se crea un cliente utilizando el documento 1001, el cual ya fue registrado en la primera prueba 
    cliente = Cliente(
        "1001",
        "Juan Perez",
        "juan2@gmail.com",
        "3101234567"
    )

    #El sistema detectará que el documento ya existe y generará una excepción
    sistema.registrar_cliente(cliente)


#Se ejecuta la prueba
ejecutar_prueba(
    "Registro de cliente duplicado",
    prueba_cliente_duplicado
)

#--------PRUEBA 4: CREACIÓN DE SALA--------
#Función que crea y registra una sala disponible
def prueba_crear_sala():

    #Se crea un objeto ReservaSala
    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        30000,
        10,
        True
    )

    #Se registra la sala en el sistem
    sistema.registrar_servicio(sala)

    #Se retorna la descripción del servicio
    return sala.describir_servicio()

#Se ejecuta la prueba
ejecutar_prueba(
    "Creación de sala",
    prueba_crear_sala
)

#--------PRUEBA 5: CREACIÓN DE EQUIPO INVÁLIDO--------
#Función que intenta crear un equipo con una cantidad negativa de unidades
def prueba_equipo_invalido():

    #La cantidad -2 no es válida.El constructor generará una excepción ValueError
    equipo = AlquilerEquipo(
        "E001",
        "Computador",
        15000,
        -2
    )

    #Esta instrucción no se ejecutará si el constructor genera la excepción
    sistema.registrar_servicio(equipo)


#Se ejecuta la prueba
ejecutar_prueba(
    "Creación de equipo con cantidad negativa",
    prueba_equipo_invalido
)

# PRUEBA 6: CREACIÓN DE ASESORÍA

#Función que crea y registra una asesoría especializada
def prueba_crear_asesoria():

    #Se crea un objeto Asesoria con datos válidos
    asesoria = Asesoria(
        "A001",
        "Asesoría de programación",
        50000,
        "Desarrollo de software",
        "Carlos Gómez"
    )

    #Se registra la asesoría en el sistema
    sistema.registrar_servicio(asesoria)

    #Se retorna la descripción de la asesoría
    return asesoria.describir_servicio()


#Se ejecuta la prueba
ejecutar_prueba(
    "Creación de asesoría",
    prueba_crear_asesoria
)

#--------PRUEBA 7: CREACIÓN DE EQUIPO VÁLIDO--------
#Función que crea y registra un equipo con una cantidad disponible válida
def prueba_crear_equipo():

    #Se crea un objeto AlquilerEquipo
    equipo = AlquilerEquipo(
        "E002",
        "Proyector",
        20000,
        3
    )

    #Se registra el equipo en el sistema
    sistema.registrar_servicio(equipo)

    #Se retorna la descripción del equipo
    return equipo.describir_servicio()


#Se ejecuta la prueba
ejecutar_prueba(
    "Creación de equipo válido",
    prueba_crear_equipo
)

#PRUEBA 8: CREACIÓN DE RESERVA
#Función que crea una reserva de sala aplicando descuento e impuesto
def prueba_crear_reserva():

    #Se busca el cliente registrado con documento 1001
    cliente = sistema.buscar_cliente("1001")

    #Se busca la sala registrada con código S001
    sala = sistema.buscar_servicio("S001")

    #Se crea la reserva con duración de 3 horas. Se aplica un descuento del 10 %. Se aplica un impuesto del 19 %
    reserva = sistema.crear_reserva(
        cliente,
        sala,
        3,
        0.10,
        0.19
    )

    #Se retorna la información de la reserva
    return reserva.mostrar_informacion()


#Se ejecuta la prueba
ejecutar_prueba(
    "Creación de reserva con descuento e impuesto",
    prueba_crear_reserva
)
#--------PRUEBA 9: CONFIRMACIÓN DE RESERVA--------
#Función que confirma la reserva R001
def prueba_confirmar_reserva():

    #Se busca la reserva por su identificador
    reserva = sistema.buscar_reserva("R001")

    #Se solicita al sistema confirmar la reserva
    sistema.confirmar_reserva("R001")

    #Se retorna la información actualizada. El estado debería ser Confirmada
    return reserva.mostrar_informacion()


#Se ejecuta la prueba
ejecutar_prueba(
    "Confirmación de reserva",
    prueba_confirmar_reserva
)
#--------PRUEBA 10: CANCELACIÓN DE RESERVA--------
#Función que cancela la reserva R001
def prueba_cancelar_reserva():

    #Se busca la reserva antes de cancelarla
    reserva = sistema.buscar_reserva("R001")

    #Se solicita cancelar la reserva
    sistema.cancelar_reserva("R001")

    #Se retorna la información actualizada
    #El estado debería ser Cancelada
    return reserva.mostrar_informacion()


#Se ejecuta la prueba
ejecutar_prueba(
    "Cancelación de reserva",
    prueba_cancelar_reserva
)
#--------PRUEBA 11: CONFIRMAR RESERVA CANCELADA--------
#Función que intenta confirmar una reserva que ya fue cancelada.
def prueba_confirmacion_incorrecta():

    #La reserva R001 ya se encuentra cancelada el sistema debe impedir que se confirme nuevamente
    sistema.confirmar_reserva("R001")


#Se ejecuta la prueba
ejecutar_prueba(
    "Intentar confirmar una reserva cancelada",
    prueba_confirmacion_incorrecta
)
#--------PRUEBA 12: SERVICIO NO DISPONIBLE--------
#Función que intenta crear una reserva sobre una sala que no está disponible
def prueba_servicio_no_disponible():

    #Se crea una sala con disponibilidad False
    sala = ReservaSala(
        "S002",
        "Sala ocupada",
        25000,
        5,
        False
    )

    #Se registra la sala en el sistema
    sistema.registrar_servicio(sala)

    #Se busca el cliente previamente registrado
    cliente = sistema.buscar_cliente("1001")

    #Se intenta realizar una reserva
    #La validación de disponibilidad generará un error
    sistema.crear_reserva(
        cliente,
        sala,
        2
    )


#Se ejecuta la prueba
ejecutar_prueba(
    "Reserva de sala no disponible",
    prueba_servicio_no_disponible
)
#Función que intenta buscar un cliente cuyo documento no está registrado
def prueba_cliente_inexistente():

    #El documento 999999 no existe se generará ElementoNoEncontrado.
    sistema.buscar_cliente("999999")


# Se ejecuta la prueba.
ejecutar_prueba(
    "Búsqueda de cliente inexistente",
    prueba_cliente_inexistente
)
#--------RESUMEN FINAL DEL SISTEMA--------
#Se imprime un encabezado para presentar los resultados finales de las operaciones
print("\n")
print("=" * 50)
print("RESUMEN FINAL DEL SISTEMA")
print("=" * 50)

#Se muestra el total de clientes, servicios y reservas
print(sistema.mostrar_resumen())
#--------LISTADO DE CLIENTES-------
#Se imprime el título del listado de clientes
print("\nCLIENTES:")

# Se recorren los clientes registrados.
for cliente in sistema.listar_clientes():

    #Se imprime cada cliente.
    print(cliente)
#--------LISTADO DE SERVICIOS--------
#Se imprime el título del listado de servicios
print("\nSERVICIOS:")

#Se recorren los servicios registrados
for servicio in sistema.listar_servicios():

    #Se llama al método describir_servicio(). El comportamiento depende del tipo de servicio, demostrando polimorfismo.
    print(servicio.describir_servicio())
#--------LISTADO DE RESERVAS--------
#Se imprime el título del listado de reservas
print("\nRESERVAS:")

#Se recorren todas las reservas registradas
for reserva in sistema.listar_reservas():

    #Se muestra la información completa de cada reserva
    print(reserva.mostrar_informacion())

    #Se imprime una línea separadora
    print("-" * 30)
#--------FINALIZACIÓN DEL PROGRAMA--------
#Se informa que todas las pruebas han terminado. Los errores ocurridos fueron capturados para evitar que interrumpieran la ejecución del programa.
print("\nEl sistema finalizó sin detenerse por errores.")