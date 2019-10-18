#--------------------------------ASPECTOS_TECNICOS------------------------------
"""
PIL (Python Image Library) va a ser utilizada ya que dentro de sus funciones uno
puede abrir y alterar imagenes. Se va exportar con el apodo 'im' para mayor
facilidad de uso.
"""
from PIL import Image as im

#-------------------------------------CLASES------------------------------------
class Esteganew:
    """
    Esteganew es una clase diseñada con la finalidad de poder esconder texto
    dentro de los bits menos significativos de los pixeles que conforman una
    imagen.
    """

    def __init__(self, nombre_imagen:str, mensaje:str, nuevo_nombre:str):
        """
        Esta clase tiene requiere en un principio como primer argumento el
        nombre de la imagen que será utilizada (con extención tipo: '.png',
        '.tiff,' .jpg'... etc.) de tipo 'str', como segundo argumento el
        mensaje que se desea esconder tambien de tipo 'str' y para el tercer
        argumento se exige un nombre para el archivo de salida tambien con
        extención y de tipo 'str'.
        """
        self.imagen = im.open(nombre_imagen, 'r')
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
            print(pixel)
            print(self.mensaje[i])
            print(lista_data[i])


            #Esta iteración convierte los valores impares (del valor R.G o B)
            #en 1 y los valores pares en 0, así formando el mensaje.
            for j in range(0,8):
                if (lista_data[i][j] == "0") and (pixel[j]%2 != 0):
                    pixel[j] -= 1

                elif (lista_data[i][j] == "1") and (pixel[j] % 2 == 0):
                    pixel[j] -= 1

            #La función va a estar diseñada para revisar el valor de la octava
            #cifra de cada pixel (la variable l.61), si el valor de esa cifra
            #es de 0 significa que debe continuar leyendo, pero si el valor de
            #la cifra es de 1 significa que el mensaje termino.
            if (i == tamano_data - 1):
                if (pixel[-1] % 2 != 0):
                    pixel[-1] -= 1
            else:
                if (pixel[-1] % 2 != 0):
                    pixel[-1] -= 1

            pixel = tuple(pixel)
            print("{}\n".format(pixel))
            # print( pixel[0:3])
            # print( pixel[3:6])
            # print( pixel[6:9])









#------------------------------------FUNCIONES----------------------------------
#------------------------------------CODIGO-------------------------------------
