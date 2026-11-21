import re #Libreria para manjo de correos y números de telefono
from entidad import Entidad
from excepciones import ClienteInvalido

#Cliente hereda de entidad 
class Cliente(Entidad):

    #Inicializador
    def __init__(self, documento, nombre, correo, telefono):

        super().__init__(documento)
        
        #verificamos que el nombre del cliente no exista
        if not nombre or not nombre.strip():
            raise ClienteInvalido("El nombre no puede estar vacío.")
        
        #validador de que nombre solo tenga letras 
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre):
            raise ClienteInvalido("El nombre contiene caracteres inválidos.")
        
        #Valida que el correo electronico tenga la estructura adecuada
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
            raise ClienteInvalido("El correo electrónico no es válido.")

        #Se usa para que el numero solo tenga 10 numeros
        if not str(telefono).isdigit() or len(str(telefono)) < 10:
            raise ClienteInvalido("El teléfono debe contener mínimo 10 dígitos.")

        #Se verifica que el documento sean solo números
        if not str(documento).isdigit():
            raise ClienteInvalido("El documento debe ser numérico.")

        #Recogemos los atributos como privados
        self.__nombre = nombre.strip()
        self.__correo = correo
        self.__telefono = str(telefono)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    #Antes de que se hagna cambios se tiene que validar que el correo tenga el formato correcto
    def actualizar_correo(self, nuevo_correo):

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", nuevo_correo):
            raise ClienteInvalido("El nuevo correo no es válido.")

        self.__correo = nuevo_correo

    #retorna la informacion del cleinte en texto
    def mostrar_informacion(self):

        return (
            f"Documento: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )

    def __str__(self):
        return self.mostrar_informacion()