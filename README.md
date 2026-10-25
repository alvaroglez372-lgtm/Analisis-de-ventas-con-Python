Los datos de las ventas se encuentran originalmente en un archivo csv (ventas.csv) en la carpeta "datos".

"Main.py" es el script principal. Al ejecutarse comienza importando los módulos y funciones necesarias (algunas proceden de los archivos situados en "mi_libreria").

Inicialmente el programa pide al usuario indicar el nombre del archivo csv de la carpeta "datos" con el que se desea trabajar. A continuación, "main.py" llama a la función "leer_csv" perteneciente al archivo "lectura.py". Esta función recibe como argumento la ruta con el nombre del archivo indicado y recupera los datos del archivo almacenándolos en una variable que devuelve como "ventas". La función cuenta con el manejo de excepciones de varios errores. Luego, el programa comprueba que existen todas las categorías nececesarias en los datos recuperados con Pandas.

Después se llama a las funciones "calculo_importe" y "ventas_totalesYcategorias" definidas en el archivo "calculos.py" perteneciente a "mi_librería".
La primera función calcula el importe de cada venta en una nueva columna llamada "importe". Para ello multiplica las unidades de cada venta por el precio unitario de cada producto.
La segunda realiza varios cálculos (el importe total, las unidades total, y los mismos datos separados por categoría).
Todas estas funciones reciben como argumento un único parámetro que representa los datos del archivo csv. Este parámetro es la variable de ventas definida anteriormente.

Tras ello el programa pregunta al usuario si desea consultar el importe total de alguna categoría concreta. Si la respuesta es "si", el programa pide que se escriba el nombre exacto de la categoría y filtra los datos para quedarse solo con una lista de las ventas de dicha categoría y calcula su importe total. A continuación vuelve a preguntar si se desean hacer más consultas. El bucle se rompe cuando la respuesta es "no".

Por último el programa pide al usuario que indique un nombre para guardar la información nueva en un archivo "parquet". Una vez indicado, se crea un archivo parquet con todos los datos en la misma carpeta "datos" donde se encontraba el archivo "csv".
Finalmente el programa recupera el archivo "parquet" y muestra los datos en la terminal. De esta manera se comprueba que se ha guardado correctamente y que se pueden recuperar los datos. 

El proyecto está organizado de manera modular ya que permite reutilizar funciones de manera más sencilla en el futuro. Además, de esta manera se puede comprender el programa de forma clara y limpia.

He utilizado la IA generativa únicamente para entender los errores que me iba lanzando la terminaly para realizar la parte de la consulta por categorías, ya que tuve problemas para utilizar los condicionales "if" aplicados al dataframe. 