import struct #para convertir entre cadenas de bytes y tipos de datos nativos de Python, como números y cadenas.
import os #determinar el tipo de una imagen y manipular la estructura de directorios

class UnknownImageFormat(Exception):
    pass

class EsteganoSize (object):

    def __init__(self,name):
        self.im = name

    def image_size(self):
        # Se supone que va a devolver (ancho,alto) de una imagen recibida
        size = os.path.getsize(self.im)
        with open(self.im) as input:
            height = -1
            widht = -1
            data = input.read(25)
            if (size >= 10) and data[:6] in ('GIF87a', 'GIF89a'):
                # GIFs
                w, h = struct.unpack("<HH", data[6:10])
                width = int(w)
                height = int(h)
            elif ((size >= 24) and data.startswith('\211PNG\r\n\032\n') and (data[12:16] == 'IHDR')):
                # PNGs
                w, h = struct.unpack(">LL", data[16:24])
                width = int(w)
                height = int(h)
            elif (size >= 16) and data.startswith('\211PNG\r\n\032\n'):
                # otros PNGs
                w, h = struct.unpack(">LL", data[8:16])
                width = int(w)
                height = int(h)
            elif (size >= 2) and data.startswith('\377\330'):
                # JPEG
                msg = "raised mientras se trataba de hacer un JPEG"
                input.seek(0)#establece la posición actual del archivo en el desplazamiento.
                input.read(2)
                b = input.read(1)
                try:
                    while (b and ord(b) != 0xDA): #La función ord () devuelve el número que representa el código Unicode de un carácter especificado.
                        while (ord(b) != 0xFF): b = input.read(1)
                        while (ord(b) == 0xFF): b = input.read(1)
                        if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                            input.read(3)
                            h, w = struct.unpack(">HH", input.read(4)) #The result is a tuple even if it contains exactly one item.
                            break
                        else:
                            input.read(int(struct.unpack(">H", input.read(2))[0])-2)
                        b = input.read(1)
                    width = int(w)
                    height = int(h)
                except struct.error:
                    raise UnknownImageFormat("StructError" + msg)
            else:
                raise UnknownImageFormat(
                    "Formato desconocido :/"
                )

        return width, height



hola = EsteganoSize("test.jpg")
print(hola.image_size())
