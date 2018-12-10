	Asignación de iconos a los diferentes establecimientos económicos, utilizando el módulo Folium en Python.

José Daniel Mejía, Janet Monserrat Partida Esquivel
Universidad de Colima, Campus Coquimatlán, Facultad de Ingeniería Civil, CP:28400.                                  
jmejia13@ucol.mx, jannypartida16@gmail.com
 
Resumen
En este proyecto se realizó un programa escrito en Python, haciendo uso de la librería Folium, princi-palmente, en donde se procesan los datos de un DENUE, para señalar espacialmente los estableci-mientos económicos ubicados en dicho archivo, mediante iconos relacionados directamente con el tipo de actividad que se desempeña en cada uno de los distintos establecimientos.
Palabras clave: Python, Folium, SHP, SIG, Cartogra-fía.

Abstract
This project was a program written in Python, making use of the Folium library, mainly, in where a DENUE data, are processed to spatially noted the economic establishments located in such file, icons directly related to the type of activity that plays in each of the different establishments.
Keywords: Python, Folium, SHP, SIG, cartography,. 

1. 	Introducción
El Directorio Estadístico Nacional de Unidades Económicas (DENUE) brinda los datos de iden-tificación, ubicación, actividad económica y tamaño de 5 millones 78 mil 737 unidades eco-nómicas activas en el territorio nacional; actuali-zados, fundamentalmente, en el segmento de los establecimientos grandes, cuyas caracterís-ticas se describen en un documento metodoló-gico.
Python no solamente es un lenguaje para escri-bir scripts, también posee soporte y estructura para realizar programas largos con muchas lí-neas de código, es un lenguaje de muy alto nivel y ofrece muchos tipos de datos y el che-queo de errores es mucho más sencillo que con otros lenguajes de programación.
Una librería es un conjunto de recursos que pueden ser utilizados por el programador para realizar determinadas operaciones. 
En este proyecto el uso de Folium, que es la librería principal, además de Pandas, trabaja con INEGI, y junto con dichas operaciones o códigos claves, nos ayuda a mapear y repre-sentar por medio de iconos algunos estableci-mientos. Dicha información que será obtenida con ayuda del DENUE.

2. Desarrollo Experimental. 
Python permite dividir programas en módulos que pueden ser reusados en otros programas escritos en Python y en otros lenguajes, pues viene con una amplia colección de módulos predefinidos que pueden ser usados como base para otros programas escritos en el mis-mo lenguaje.
Pandas es una librería de Python destinada al análisis de datos, que proporciona unas estruc-turas de datos flexibles y que permiten trabajar con ellos de forma muy eficiente, en cambio Folium es una potente biblioteca de visualiza-ción de datos en Python que se creó principal-mente para ayudar a las personas a visualizar datos geoespaciales. 

2.1. Manejo de Datos. 
Después de importar las librerías, trabajamos con Pandas nos permitió abrir y tomar los datos del archivo csv del DENUE, específicamente las coordenadas (latitud y longitud) que nos sirvió para poder marcar los puntos de acuerdo a las ubicaciones de los establecimientos, además de su nombre.
En la instrucción “file.head”, se especifica canti-dad de establecimientos que se leen. Esta pue-de ser editada como un comentario si se quie-ren leer todos. Para la prueba, solo tomamos en cuenta los primeros 5.
Creamos el mapa con la instrucción “fo-lium.map()”, partiendo del centro del estado de Colima.
Finalmente, con un ciclo for seleccionamos los puntos a mapear e ingresamos su nombre, se-gún corresponde.
El DENUE del que nos basamos arrojaba mu-chos puntos, lo que hacía que su proceso fuera más lento. Al presentarnos con dicho problema, optamos por reducir el número de puntos (solo para realizar pruebas) a procesar a los de la zona conurbada del estado de Colima.
Como ya se mencionó anteriormente, folium trabaja con coordenadas geográficas y en nues-tro caso, la información manejada en el DENUE tiene el formato necesario, lo que facilitó su uso.
Cuando descargamos el archivo, pudimos ver que los datos estaban sin un orden concreto y por ello tuvimos que buscar la forma de “lim-piarlos” y trabajar con ellos, así, al momento de procesarlos los errores fueran mínimos
Optamos por separar el programa por partes y hacer pruebas con pocas líneas de código, de esta forma íbamos verificando los errores que teníamos y su solución era más sencilla.

3. Análisis de Resultados. 
Cumpliendo el proyecto lo que obtuvimos fue el mapa con los puntos y nombre de cada esta-blecimiento. Además de que es posible mostrar (en la pantalla) las columnas de la información que se genera en el mapa.

Podemos notar que lo más importante para lograr mapear correctamente los puntos son la “latitud” y “longitud”, además de tener la certeza del centroide que se está tomando porque será nuestra referencia.
 
4. Conclusiones.
Al finalizar el proyecto, comprendimos la impor-tancia que tienen estas librerías, principalmente Folium y como esta puede ser utilizada a lo largo de proyectos en los que sean necesarios la representación de datos, además de la rela-ción que tiene Python y la programación con otras materias.

5. Bibliografías.
•	Asesoría del Dr. Solano B, R. Facultad de Ingeniera Civil, U de C.
•	Lasset, A. (GiITHub) https://medium.com/@austinlasseter/using-folium-to-generate-a-simple-map-of-your-pandas-data-87ddc5d55f8d
•	DENUE, (INEGI) http://www.beta.inegi.org.mx/servicios/api_denue.html
•	Rieke, C. (GiITHub) https://medium.com/@chrieke/essential-geospatial-python-libraries-5d82fcc38731
•	FOLIUM/JSON https://pypi.org/project/folium/

