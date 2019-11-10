#--------------------------------ASPECTOS_TECNICOS------------------------------
"""
PIL (Python Image Library) va a ser utilizada ya que dentro de sus funciones uno
puede abrir y alterar imagenes. Se va exportar con el apodo 'im' para mayor
facilidad de uso.
"""
from os import system, name
from time import sleep
from PIL import Image as im
from AESCipher import enCRYptar, deCRYptar, clear



#-------------------------------------CLASES------------------------------------
class Esteganew:
    """
    Esteganew es una clase diseñada con la finalidad de poder esconder texto
    dentro de los bits menos significativos de los pixeles que conforman una
    imagen.
    """


    def __init__(self, nombre_imagen:str, mensaje = None, nuevo_nombre = None ):
        """
        Esta clase tiene requiere en un principio como primer argumento el
        nombre de la imagen que será utilizada (con extención tipo: '.png',
        '.tiff,' .jpg'... etc.) de tipo 'str', como segundo argumento el
        mensaje que se desea esconder tambien de tipo 'str' y para el tercer
        argumento se exige un nombre para el archivo de salida de tipo 'str'.
        """
        try:
            self.imagen = im.open(nombre_imagen, 'r')
        except:
            clear()
            print("Lo sentimos, pero el proceso no puede ser terminado :(")
            sleep(5)
            clear()
            raise SystemExit

        self.copia_img = self.imagen.copy()
        self.mensaje = mensaje
        self.pixeles =  self.copia_img.getdata()
        self.nuevo_nombre = nuevo_nombre


    def generar_data(self):
        """
        Esta función se encarga de transformar el mensaje a binario. Lo que hace
        es adjuntar a una lista el valor de cada caracter, el cual se obtiene en
        un principio transformandolo a su valor en Unicode, y luego este a
        binario.
        """

        lista_data = []
        for i in self.mensaje:
            lista_data.append(format(ord(i), '08b'))
        return lista_data

    def modificar_pixeles(self):
        """
        La razón de esta función es la de convertir los pixeles necesarios de la
        imagen (según lo largo del mensaje) en nuvos pixeles alterando el valor
        RGB de cada pixel reduciendolo en una unidad.
        """

        lista_data = self.generar_data()
        tamano_data = len(lista_data)
        pixel = self.pixeles
        # pixel es un 'Generator' pues es una iteración que solo guarda el
        #valor individual de cada iteración. Se usa el '__next__' para
        #decirle a el 'Generator' que olvide el valor actual y utilice
        #el siguiente.
        imagen_data = iter(pixel)

        #Este ciclo for esta para que según el tamaño del mensaje a adjuntar se
        #editen los valores RGB de cada pixel, reduciendolo en una unidad.
        for i in range(tamano_data):
            #Extrae del 'Generator' los valores de 3 pixeles de forma simultanea.
            pixel = [valor for valor in imagen_data.__next__()[:3]+
                                        imagen_data.__next__()[:3]+
                                        imagen_data.__next__()[:3]]


            #El proceso de alteración de los pixel comienza comparando el
            #valor binario de cada letra con los valores de cada 3 pixeles
            #(R,G,B,R,G,B,R,G,B) ,utilizando los primeros 8 valores para
            #esconder el mensaje y el ultimo para definir la longitud del
            #mensaje al momento de decodificarlo.

            #En la primera parte compara cada bit de cada letra con su
            #respectiva posicion en la tupla (R,G,B,R,G,B,R,G,B), si el
            #valor del bit es igual a '0' y el valor de color en la tupla
            #dividido en 2 deja reciduo, se le resta una unidad al valor
            #de la tupla, si el valor del bit es igual a '4' y el valor
            #de color en la tupla dividido en 2 no deja reciduo, se le
            #resta una unidad al valor de la tupla.
            for j in range(0,8):

                if (lista_data[i][j] == "0") and (pixel[j]%2 != 0):
                    pixel[j] -= 1

                elif (lista_data[i][j] == "1") and (pixel[j] % 2 == 0):
                    if pixel[j] != 0:
                        pixel[j] -= 1
                    else:
                        pixel[j] += 1

            #Este condicional revisa si el mensaje ya codificado completamente,
            #para que el decodificador sea capaz de interpretarlo se acuerda
            #si el ultimo valor de la tupla (R,G,B,R,G,B,R,G,B) es par el
            #mensaje continua y si el valor es impar, significa que el mensaje
            #ya a acabado.
            if (i == tamano_data - 1):
                if (pixel[-1] % 2 == 0):
                    pixel[-1] -= 1
            else:
                if (pixel[-1] % 2 != 0):
                    pixel[-1] -= 1

            pixel = tuple(pixel)
            yield pixel[0:3]
            yield pixel[3:6]
            yield pixel[6:9]


    def cambiar_pix(self):
        """
        Esta función se encarga de modificar ya en la nueva image los valores
        de los pixeles. A partir de las cordenadas (x, y) de la imagen.
        """

        #El ancho de la imagen
        w = self.copia_img.size[0]
        (x, y) = (0, 0)

        for pix in self.modificar_pixeles():
            self.copia_img.putpixel((x,y),pix)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def codificar(self):
        """
        La función codificar() esta dada para retornar un archivo en
        formato '.png', con el mensaje ya escondido.
        """

        if (self.mensaje == None):
            raise Exception("Necesitas un mensaje si quieres codificar.")
        elif (self.nuevo_nombre == None):
            raise Exception("Necesitas un nuevo nombre para el archivo si quieres codificar.")
        else:
            self.cambiar_pix()
            self.copia_img.save("{}.png".format(self.nuevo_nombre), "PNG")

    def decodificar(self):
        """
        Esta función cumple la labor de retornar el mensaje oculto dentro de
        la imagen.
        """
        if (self.mensaje != None):
            raise Exception("No necesitas un mensaje si quieres decodificar.")
        elif (self.nuevo_nombre != None):
            raise Exception("No necesitas un nuevo nombre para el archivo si quieres decodificar.")
        else:
            mensaje_secreto = ""
            imagen_data = iter(self.imagen.getdata())

            while (True):
                pixeles = [valor for valor in imagen_data.__next__()[:3]+
                                            imagen_data.__next__()[:3]+
                                            imagen_data.__next__()[:3]]

                str_binario = ""

                for i in pixeles[:8]:
                    if (i % 2 == 0):
                        str_binario += "0"
                    else:
                        str_binario += "1"

                mensaje_secreto += chr(int(str_binario, 2))
                if pixeles[-1] % 2 != 0:
                    return mensaje_secreto

#------------------------------------FUNCIONES----------------------------------


def main():

    clear()
    print("Bienvenido a Esteganew")
    print("{}".format("="*22))
    respuesta0 = input("Marca 1 si quieres codificar o 2 si quieres decodificar.\n--> ")

#=========================== C O D I F I C A R =================================

    if (respuesta0 == "1"):
        clear()
        nombre_imagen = input("Inserta el nombre de la imagen que desea codificar.\n(Es necesari escribirla con el formato('.png', '.jpg', '.tiff'... etc)\n--> ")
        clear()
        print("Inserta el mensaje que quiere encriptar.")
        mensaje = input("(El mensaje debe ser menor a 4095 caracteres)\n--> ")
        while True:
            counter = 1
            clear()
            for i in range(len(mensaje)):
                counter += 1
            if counter > 4095:
                print("Recuerda que el limite son 4095 caracteres contando simbolos y espacios.")
                print("""                        INTENTLO DE NUEVO""")
                sleep(4)
                clear()
                print("Inserta el mensaje que quiere encriptar.")
                mensaje = input("(El mensaje debe ser menor a 4095 caracteres)\n--> ")
            else:
                break


        clear()
        mensaje = enCRYptar(mensaje)
        nuevo_nombre = input("Inserta un nombre para el archivo de salida.\n--> ")
        imag_cod = Esteganew(nombre_imagen,mensaje,nuevo_nombre)
        imag_cod.codificar()
        clear()
        print("""                  ============================================""")
        print("""                  Muchas Gracias El Trabajo Ha Sido Completado""")
        print("""                  ============================================""")
        sleep(5)
        clear()

#=========================== D E C O D I F I C A R =============================

    elif (respuesta0 == "2"):
        clear()
        nombre_imagen = input("Inserta el nombre de la imagen que desea decodificar.\n(Es necesari escribirla con el formato('.png', '.jpg', '.tiff'... etc)\n--> ")
        imag_dec = Esteganew(nombre_imagen)
        clear()
        archivo_clave = input("Ya tenemos tu mensaje, escribe el nombre del archivo con la clave para que te retornemos el mensaje:\n")
        mensaje_pre = imag_dec.decodificar()
        mensaje_post = deCRYptar(mensaje_pre,archivo_clave)

        # ======= RETORNAR ARCHIVO ========
        clear()

        while True:
            nombre_archivo = input("Inserta un nombre para el archivo de salida.\n")
            break

        archivo = open("{}.txt".format(nombre_archivo), "w")
        archivo.write(mensaje_post)
        archivo.close()
        clear()
        print("""                  ============================================""")
        print("""                  Muchas Gracias El Trabajo Ha Sido Completado""")
        print("""                  ============================================""")
        sleep(5)
        clear()

#============================== E R R O R ======================================

    else:
        clear()
        print("Esa opción no se encuentra disponible")
        sleep(3)
        raise main()

#------------------------------------CODIGO-------------------------------------
if __name__ == '__main__':
    main()
