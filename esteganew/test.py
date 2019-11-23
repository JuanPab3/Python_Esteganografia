"""
Para poder implementar esté codigo, porfavor instalar la libreria esteganew de la forma:
           sudo pip3 install esteganew
"""

from Esteganew.esteganew import *
#------------------------------------FUNCIONES----------------------------------


def main():

    clear()
    print("Bienvenido a Esteganew")
    print("{}".format("="*22))
    respuesta0 = input("Marca 1 si quieres codificar o 2 si quieres decodificar.\n--> ")

#=========================== C O D I F I C A R =================================

    if (respuesta0 == "1"):
        clear()
        nombre_imagen = input("Inserta el nombre de la imagen que desea codificar.\n(Es necesario escribirla con el formato('.png', '.jpg', '.tiff'... etc)\n--> ")
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
        print("""                  =================================================""")
        print("""                  Se ha guardado un archivo de numbre miLlave.key
                  si desea combiarle el nombre, no cambie el '.key'.""")
        print("""                  =================================================""")
        sleep(8)

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
        archivo_clave = input("Ya tenemos tu mensaje, escribe el nombre del archivo con la clave para que te retornemos el mensaje:\n--> ")
        mensaje_pre = imag_dec.decodificar()
        mensaje_post = deCRYptar(mensaje_pre,archivo_clave)

        # ======= RETORNAR ARCHIVO ========
        clear()

        while True:
            nombre_archivo = input("Inserta un nombre para el archivo de salida.\n--> ")
            break

        archivo = open("{}.txt".format(nombre_archivo), "w")
        archivo.write(mensaje_post)
        archivo.close()
        clear()
        print("""                  ============================================""")
        print("""                  Muchas Gracias El Trabajo Ha Sido Completado""")
        print("""                  ============================================""")
        sleep(5)
        print("""                  ============================================""")
        print("""                     Su mensaje se ha guardado en un archivo
                    '.txt' dentro de la carpeta donde se esta
                                corriendo el programa.""")
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
