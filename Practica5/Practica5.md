### Practica 5. Replicación de bases de datos MySQL

----------

> Antes de nada hay que decir que esta práctica ha supuesto mucho tiempo y ha dado muchos problemas :rage:. Por eso es más que probable que en las capturas de ejemplo se observen fallos que después sí fueron corregidos para que la práctica funcionase. De hecho, esta práctica funciona completa tanto la parte obligatoria como la opcional :sunglasses:. 
> Como ejemplo, al principio no me di cuenta y creé la base de datos en el equipo 2 como MASTER, lo cual va contra el sentido común :sweat_smile:. Esto en las capturas finales está solucionado :relieved:.

Lo primero que hay que tener en cuenta para esta práctica es que tienes que tener instalado MySQL en tu máquina y saberte la contraseña de root.
Una vez con esto nos podemos poner manos a la obra.
Lo primero es crear en una de las máquinas (la que consideres master) una base de datos e introducir algunos datos.

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica5/capturas/a%C3%B1adir%20datos%20a%20tabla.tiff)

Lo siguiente es copiar **el contenido** de esta base de datos "tal cual" a la base de datos del equipo que se considere slave. Para eso hay que crear antes en el slave una base de datos. 

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/crear%20base%20de%20datos%20equipo%201.png?raw=true)

La copia de datos "manual" entre bases de datos MySQL es como sigue:

 1. Generar archivo `.sql` con `mysqldump`.
 2.  Copiar como más te guste este archivo al quipo slave.
 3. Otra vez con `mysqldump`, volcar el contenido del archivo a la base de datos del slave.

Obviamente tenemos que asegurarnos de que el iptables nos permite el envío de paquetes, ya que en la práctica anterior nos denegaba todo lo que no fuese por los puertos 80 y 443 :grin:. Yo he copiado el archivo con `scp`.

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/scp%20de%20base%20de%20datos%20tras%20reset%20iptables.png?raw=true)

Ya tenemos las bases de datos con los mismos datos:

![](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/datos%20replicados.png?raw=true)

Ahora viene lo interesante, la **replicación**. Vamos a empezar con la **maestro-esclavo**.

Tenemos que modificar el achivo `/etc/mysql/mysql.conf.d/mysqld.cnf` tal y como dice el guión.
Después hay que crear en nuestro maestro un usuario para que el esclavo se identifique como él.

> Ejemplo:
> 
> Tenemos dos amigos: PEPE:older_man: y ANTONIO:cop:, cada uno con un ordenador.
> 
> ANTONIO:cop: quiere conectarse al ordenador de PEPE:older_man:.
> 
> PEPE:older_man: debe crear el usuario ANTONIO:cop: en su equipo para que se identifique.

User esclavo:

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/user%20esclavo%20creado.png?raw=true)

Se le dan permisos:

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/dar%20permisos%20a%20esclavo.png?raw=true)

Al intentar hacer la replicación nos muestra este fallo:

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica5/capturas/error%20sincronizacion%20sql.tiff)

Este fallo es debido a que al principio de los tiempos, estas máquinas virturales habían sido clonadas una de la otra. El UUID que identifica de manera única a cada servidor MySQL coincidía, por tanto se creía que te querías conectar a la misma máquina (cosa que sería absurdo). Esto lo solucionamos poniendoun UUID válido en el archivo `/var/lib/mysql/auto.cnf` o borrándolo y esperando a que se cree nuevo por el sistema.

Pero después salía otro error:

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica5/capturas/sncronizacion%20incorrecta.tiff)

Este fallo podía ser de dos cosas:

 1. O bien de la conexión de red.
 2. O bien de la gestión del usuario, los permisos y el acceso a la base de datos.

Tras darle un par de vueltas descubro que la conexión está bien, así que toca ir a lo segundo que es lo complicado :weary::weary::weary:.
Después de un rato, decido ir a lo seguro y borré todo lo creado en la base de datos. TODO. Toda la base de datos entera. Creé una nueva y creé un usuario "prueba" nuevo.

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/Captura%20de%20pantalla%202017-05-22%20a%20la%28s%29%2019.03.05.png?raw=true)

Esta vez, funcionó :clap::clap::clap::clap:.

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/Captura%20de%20pantalla%202017-05-23%20a%20la%28s%29%2013.00.48.png?raw=true)

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica5/capturas/Captura%20de%20pantalla%202017-05-23%20a%20la%28s%29%2013.03.01.png?raw=true)

Para la **parte opcional**, se pide que la replicación sea **maestro-maestro**.

> Ejemplo:
> 
> Tenemos dos amigos: CARLOS:man: y CARLA:woman:, cada uno con un ordenador.
> 
> A CARLOS:man: le decimos que es esclavo y que el maestro es CARLA:woman:.
> 
> A CARLA:woman: le decimos también que es esclava y que el maestro es CARLOS:man:.
> 
> Su relación se basa en una mentira, pero ellos viven felices creyendo que son maestro-maestro :couplekiss: :heart:.   :couplekiss: :couple_with_heart: