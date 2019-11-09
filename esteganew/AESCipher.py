#--------------------------------ASPECTOS_TECNICOS------------------------------
from cryptography.fernet import Fernet

#-------------------------------------CLASES------------------------------------

#------------------------------------FUNCIONES----------------------------------
def llave():
    """
    Con esta función se genera una llave para empezar el proceso de encriptación,
    la cual es de tipo "bytes".
    """
    llave = Fernet.generate_key()
    with open("miLlave.key", "wb") as k:
        k.write(llave)
    return llave

def enCRYptar(mensaje):

    mensaje_cod = mensaje.encode()
    allave = llave()
    objeto_crypto = Fernet(allave)
    mensaje_encript =objeto_crypto.encrypt(mensaje_cod)
    return mensaje_encript.decode()

def deCRYptar(mensaje,nombre_archivo):
    try:
        archivo = open(nombre_archivo, "rb")
    except FileNotFoundError or UnboundLocalError:
        raise Exception("Lo sentimos, pero no fue posible extraer el mesaje. :(")
    clave = archivo.read()
    archivo.close()
    mensaje = mensaje.encode()
    objeto_crypto = Fernet(clave)
    decriptando = objeto_crypto.decrypt(mensaje)
    decodificado = decriptando.decode()
    return decodificado








#------------------------------------CODIGO-------------------------------------
