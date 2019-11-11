# Python y Esteganografía



## Resumen Ejecutivo

La protección de datos se torna en un derecho fundamental si se tienen en cuenta los avances acelerados que se han evidenciado en el mundo digital hasta ahora; lo anterior es clave puesto que se debería garantizar la privacidad de los individuos. En ese sentido, se puede inferir que nos encontramos en un momento crítico de seguridad de datos por lo tanto se genera un creciente interés por la investigación, generación, difusión y utilización de herramientas de protección de información. Así, entra en juego la esteganografía como ciencia que perfecciona las técnicas y tecnologías en los procesos de oculta-miento de la información. Si bien, es un tema extenso, en donde existen múltiples formas, herramientas, técnicas y métodos que permiten la manipulación de mensajes o contenido oculto con el fin de que un receptor reciba los datos; la Esteganografía permite escribir y esconder la información en archivos de cualquier tipo de tal forma que el contenedor funcionará y lucirá igual, sin embargo, en la versión final tendrá información oculta que puede ser extraída.

Basándonos en lo anterior este proyecto logró generar una herramienta de línea de comandos que permite esconder texto en imágenes y cifrar los archivos finales, a través del método de los bits o menos significativos de los pixeles que conforman la imagen para finalmente obtener la imagen con el mensaje oculto, posible por la investigación de teorías y técnicas de esteganografía mediante el lenguaje de programación de Python.

En el periodo de tiempo abarcado desde el informe de segundo avance hasta la entrega final fue posible generar la herramienta que implementa la esteganografia con éxito. Además, se logró implementar otro objetivo que no se había contemplado en un inicio y le añade más seguridad a la encriptación de la información, el cual se basa en una clave única para poder descifrar la información ya ocultada. Por un lado, uno de los objetivos de nuestro proyecto era el desarrollo web de la herramienta de esteganografía, sin embargo, con el fin de poder generar resultados satisfactorios en el periodo de tiempo acordado se planteó una salida amigable y de fácil interacción del programa con el usuario. Porotro lado, fue posible implementar funciones que harán de nuestro proyecto una herramienta más completa, óptima y de mejor comprensión como el método de cifrado y la posibilidad de hacer uso de la misma en los diferentes formatos de imágenes existentes.

En términos de investigación, hubo un avance satisfactorio en cuanto a los objetivos propuestos en las primeras entregas pues se logró profundizar el alcance de la herramienta generada y así mismo las diversas técnicas que nos permiten llevarla a cabo, pues es claro que a pesar de no ser una técnica nueva puede ser acunada a diversas tecnologías que se encuentran actualmente.

Por otro lado, en el proceso de la terminación del proyecto se presentaron dificultades pero sobre todo cambios en la estructura base de nuestros objetivos iniciales. Por un lado, la practicidad y eficacia que se pretende desarrollar con las técnicas de ocultar un mensaje en una imagen son mayores en el código final. Además, como se mencionó anteriormente desarrollar y solucionar nuestro problema base se puede lograr a partir de distintos caminos cada uno de ellos diferentes en dificultad y completud. No obstante, se acogió un método optimo, de fácil comprensión y que se adecuara tanto a los
conocimientos vistos hasta ahora como los adquiridos a lo largo del proceso de investigación y avance del proyecto. Es decir, lo que hace innovador este proyecto es que se basa en una guía completa de cómo se realiza el proceso desde un principio, es decir, el oculta miento del mensaje y así mismo el des-ocultarlo a través de Python. A partir de lo anterior, es clave tener en cuenta que se optó por generar un código completo con el fin de no apegarnos totalmente a una técnica (además de las de manipulación de imágenes) ya elaborada, que optimizaría el resultado.


## Funcionalidad de la herramienta

Basándonos en la tesis inicial de la vulnerabilidad de la información, esta herramienta permite al usuario interactuar sin el recelo que proviene de una posible censura o interceptación de datos pues se genera como un instrumento con la intención principal de esconder la información en una imagen y sobre todo logra retornar dicha información en una imagen visualmente idéntica.

En ese sentido el programa realizado se basa en el algoritmo base donde en primer lugar el usuario tiene la opción de cifrar o descifrar el mensaje de una imagen, según sea el caso, en segundo lugar se ingresa el medio de portada el cual refiere al archivo en el cual se desea disponer la información. En caso de que el usuario seleccione la opción de descifrar, el algoritmo devuelve la información oculta del medio de portada recibido; en caso, de que el usuario seleccione la opción de cifrar en tercer lugar ingresa el mensaje (con una longitud limitada a 4095 bytes, por cuestión de la encriptación) y el programa es capaz de generar una imagen idéntica con formato PNG pero ahora con la información que se quería ocultar en ella.

Como se mencionó anteriormente y basándonos en el proceso que elabora el programa Esteganografía, fue posible dar solución a la descripción del problema que se planteó en un principio a partir del método de esteganografia en imágenes. Es necesario añadir que no es necesario ocultar el mensaje en el archivo original en absoluto. Por lo tanto, no es necesario editar el archivo original, es decir, es difícil detectar nada. Si una parte determinada del mensaje se somete a una manipulación sucesiva a nivel de bits para generar el texto cifrado, entonces no hay evidencia en el archivo original que demuestre que está siendo utilizada por un tercero.


## Descripción de la herramienta

Al acudir a la definición científica de esteganografía podemos obtener que es el arte de ocultar información en archivos de imágenes, sonidos o en canales encubiertos a través de métodos y técnicas análogas o computacionales. En este caso, abarcamos los métodos en imágenes, en ese sentido, se refiere a la técnica de ocultar los mensajes o texto deseado en archivos de imágenes por medio de un mapa de bits, cambiando el valor de los bits que menos afectan la apariencia de la imagen.

Puesto que los colores que se reflejan en una imagen se ven representados por la cantidad de bits que disponga, en el caso de las fotografías a color, cada pixel tiene 24 bits de información 8 bits para cada color dentro del mapa de color RGB (rojo, verde, azul), generando así 2^24 posibles tonos distintos de color. En ese sentido, si cambia un bit (el menos significativo) el cambio no será perceptible y no ocasiona un cambio radical en la figura y por tal motivo no es apreciable por el ojo humano.

Así, fue posible desarrollar la clase Esteganew en Python la cual permitió generar el programa de manera clara y ordenada. En un principio el algoritmo está dividido en dos partes: cifrado y descifrado; por un lado, al cifrar la clase tiene como finalidad el poder esconder texto dentro de los bits menos significativos de los pixeles que conforman la imagen, teniendo en cuenta lo anterior se requieren los argumentos enunciados en la sección de funcionalidad de la herramienta, es decir, el medio de portada, el mensaje a ocultar y el nombre del archivo de salida. Ahora bien, la modificación de pixeles es
posible a partir de funciones que nos permiten en primer lugar transformar el mensaje a binario y después convertir los pixeles necesarios de la imagen (según el largo del mensaje) en nuevos pixeles alternando el valor RGB de cada pixel y reduciéndolo en una unidad. Finalmente, a partir de lasfunciones de codificar y decodificar de la clase es posible ya sea  el caso retornar un archivo en formato PNG con el mensaje ya escondido o retornar el mensaje oculto dentro de la imagen.

## Herramientas de programación

Las ventajas que trajo consigo el lenguaje de Python3 para el desarrollo de este proyecto se basan en una estructura de código natural y de fácil lectura. Una de las herramienta clave para el desarrollo de Esteganografía fue la librería gratuita PIL(Python Imagin Library) la cual está destinada al procesamiento de imágenes, es decir, nos permitió la edición de imágenes directamente desde Python. Soporta los formatos más comunes de imágenes como GIF, JPEG Y PNG. Por otro lado, se acudió a la librería cryptography.fernet para el desarrollo del cifrado y descifrado de los mensaje y que se codifiquen o decodifiquen según sea el caso, en las imágenes, dicha librería nos proporciona el algoritmo AES que considera el estado de la técnica para un cifrado óptimo. Finalmente, para el modulo de sistema se hizo uso de os el cual nos permite acceder a funcionalidades dependientes del Sistema Operativo.

---
### Contacto

El equipo está integrado por:

- [Juan Pablo Sierra Useche](https://github.com/JuanPab3)
- [Nataly Alejandra Sarmiento Ospina](https://github.com/naso071699)
__ __ __ __

muchas gracias *<3*
