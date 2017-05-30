### Practica 5. Replicación de bases de datos MySQL

----------

> Antes de nada hay que decir que esta práctica ha supuesto mucho tiempo y ha dado muchos problemas :rage:. Por eso es más que probable que en las capturas de ejemplo se observen fallos que después sí fueron corregidos para que la práctica funcionase. De hecho, esta práctica funciona completa tanto la parte obligatoria como la opcional :sunglasses:. 
> Como ejemplo, al principio no me di cuenta y creé la base de datos en el equipo 2 como MASTER, lo cual va contra el sentido común :sweat_smile:. Esto en las capturas finales está solucionado :relieved:.

Lo primero que hay que tener en cuenta para esta práctica es que tienes que tener instalado MySQL en tu máquina y saberte la contraseña de root.
Una vez con esto nos podemos poner manos a la obra.
Lo primero es crear en una de las máquinas (la que consideres master) una base de datos e introducir algunos datos.

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica5/capturas/a%C3%B1adir%20datos%20a%20tabla.tiff)

Lo siguiente es copiar **el contenido** de esta base de datos "tal cual" a la base de datos del equipo que se considere slave. Para eso hay que crear antes en el slave una base de datos. 
La copia de datos "manual" entre bases de datos MySQL es como sigue:

 1. Generar archivo `.sql` con `mysqldump`.
 2.  Copiar como más te guste este archivo al quipo slave.
 3. Otra vez con `mysqldump`, volcar el contenido del archivo a la base de datos del slave.

Obviamente tenemos que asegurarnos de que el iptables nos permite el envío de paquetes, ya que en la práctica anterior nos denegaba todo lo que no fuese por los puertos 80 y 443 :grin:. Yo he copiado el archivo con `scp`.

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/scp%20de%20base%20de%20datos%20tras%20reset%20iptables.png?raw=true)