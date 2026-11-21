
#Esta Exceoxion es propia del sistema, para errores generales
class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""
    pass

#Excepecion cuando los datosd e un client no cumple con las validaciones
class ClienteInvalido(ErrorSoftwareFJ):
    """Error relacionado con datos inválidos del cliente."""
    pass

#Excepcion para cuando se crea un cliente y este ya existe
class ClienteDuplicado(ErrorSoftwareFJ):
    """Error cuando un cliente ya se encuentra registrado."""
    pass

#Excepcion cuando los datsp de un servicio son incorrectos
class ServicioInvalido(ErrorSoftwareFJ):
    """Error relacionado con la creación de servicios."""
    pass

#Excepcion al usar un servicio que no se encuentre disponible.
class ServicioNoDisponible(ErrorSoftwareFJ):
    """Error cuando un servicio no tiene disponibilidad."""
    pass

#Controla erores durante la creacion, que tienen algun tipo de modificacion 
class ReservaInvalida(ErrorSoftwareFJ):
    """Error relacionado con las reservas."""
    pass

#Excpecion en caso tal de hacer una operacion que no corresponde al estado de la resrva     
class EstadoReservaInvalido(ErrorSoftwareFJ):
    """Error al intentar realizar una operación no permitida."""
    pass

#Excepcion para errores en lso calculos
class ErrorCalculo(ErrorSoftwareFJ):
    """Error en el cálculo de costos."""
    pass

#En caso tal de no encontrar ningun cliente, servicio o reserva
class ElementoNoEncontrado(ErrorSoftwareFJ):
    """Error cuando un elemento no existe en el sistema."""
    pass