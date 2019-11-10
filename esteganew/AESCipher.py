#--------------------------------ASPECTOS_TECNICOS------------------------------
from os import system, name
from time import sleep


def clear():
    """
    Utiliza la libreria os.system para poder limpiar la pantalla de la terminal.
    """

    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')

try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    system("gnome-terminal -e 'bash -c \"sudo pip3 install cryptography; exec bash\"'")
    clear()
    raise SystemExit
"""
El tipo de encriptación Fernet toma un mensaje codificado a bytes, el tiempo
actual y una llave de 256 bits, retornando un toquen que es una representación
indesifrable e inalterable sin el archivo llave que se implemento en un principio.

Raises:
    ModuleNotFoundError:    Si en el sistema no está instalada la librería
                            cryptography, el la exepción utilisa la librería
                            os para llamar a la terminal y ordenar la instalación
                            de la librería. Luego cierra el programa.

"""


#-------------------------------------CLASES------------------------------------

#------------------------------------FUNCIONES----------------------------------
def llave():
    """

    Con esta función se genera una llave para empezar el proceso de encriptación,
    la cual es de tipo "bytes", la cual es necesaria para poder crear un mensaje
    encriptado.

    Returns:
        bytes.Doc:  no solo retorna un valor de tipo 'bytes', sino que además
                    retorna un archivo necesario para desencriptar los valores
                    encriptados con la función 'enCRYptar()'.

    """
    llave = Fernet.generate_key()
    with open("miLlave.key", "wb") as k:
        k.write(llave)
    return llave

def enCRYptar(mensaje):
    """
    Esta se encarga de recibir un mensaje de tipo str, y apartir de la función
    'llave()', procesos de codificación nativos de python y el modulo de
    encriptación 'Feret' de la librería 'cryptography.fernet'

    Args:
        mensaje (str): es el mmensaje que va a ser encriptado.

    Returns:
        str: mensaje ya encriptado.

    """

    mensaje_cod = mensaje.encode()
    lLave = llave()
    objeto_crypto = Fernet(lLave)
    mensaje_encript =objeto_crypto.encrypt(mensaje_cod)
    return mensaje_encript.decode()

def deCRYptar(mensaje,nombre_archivo):
    """
    Se encarga de recibir un mensaje encriptado de tipo str y el nombre de un
    archivo con extención '.key', luego por medio de la función 'open()' nativa
    de python extrae el texto del archivo '.key' para aplicar  funciones del
    modulo Fermet, que ayudan a recuperar el mensaje encriptado.

    Args:
        mensaje (str):  Mensaje previamente retornado por la función 'enCRYptar()'.

        nombre_archivo (str):   Nombre del archivo generado por la función
                                'enCRYptar()', el cual porr default es
                                'miLlave.key' del cual el nombre se puede
                                cambiar pero no la extención '.key'.

    Returns:
        str: Mensaje ya decriptando

    Raises:
        FileNotFoundError or UnboundLocalError: si el archivo que se presenta no
        existe o no es el indicado para la imagen, se imprime un mensaje, avisando
        que no se logró hacer la desencripción.

    """

    try:
        archivo = open(nombre_archivo, "rb")
    except FileNotFoundError or UnboundLocalError :
        clear()
        print("Lo sentimos, pero no fue posible extraer el mesaje. :(")
        sleep(5)
        clear()
        raise SystemExit

    clave = archivo.read()
    archivo.close()
    mensaje = mensaje.encode()
    objeto_crypto = Fernet(clave)
    try:
        decriptando = objeto_crypto.decrypt(mensaje)
    except:
        clear()
        print("Lo sentimos, pero no fue posible extraer el mesaje. :(")
        sleep(5)
        clear()
        raise SystemExit
    decodificado = decriptando.decode()
    return decodificado

#------------------------------------CODIGO-------------------------------------
