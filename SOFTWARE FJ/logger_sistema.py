import logging #Importamos libreria logging para administar los registros y errores del sistema
import os #Se impoort para crear directorios cuando no existan

#
class LoggerSistema:

    def __init__(self):

        #Se crea la carperta logs en caso de que ya esta exista no va generar errores
        os.makedirs("logs", exist_ok=True)

        #Se configura el sistema de logging
        logging.basicConfig(

            #Nombre y ubicacion del archivo que llevara el resgistro
            filename="logs/software_fj.log",

            #Almacenara todo DEBUG, INFO, WARNIGN, ERRO Y CRITICAL
            level=logging.DEBUG,

            #Se define el formato de cada registro, inlcuyendo fecha, nivel del mensaje y contenido
            format="%(asctime)s | %(levelname)s | %(message)s",

            #Se establece para admintir caracteres españoles
            encoding="utf-8",

            #Permite reemplazar configuraciones anteriores de loggin cuando se inicializa esta clase
            force=True
        )

        #Se botiene un logger indentificado con el nobre SOFTWAREFJ para utilizarlo en el sistema
        self.logger = logging.getLogger("SoftwareFJ")

    #INFO indica que una oepracion se realizo o que ocurrio algun evento relevante
    def info(self, mensaje):
        self.logger.info(mensaje)

    #WARNING indica un situacion que merece atencion
    def warning(self, mensaje):
        self.logger.warning(mensaje)

    #ERROR cuando las operaciomes fallan
    def error(self, mensaje):
        self.logger.error(mensaje)

    #CRITICAL cuando hay errores muy graves
    def critical(self, mensaje):
        self.logger.critical(mensaje)

    #Muestra la excepcion que se est utilizando y el mensaje que esta dejando
    def exception(self, mensaje):
        self.logger.exception(mensaje)