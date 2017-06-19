### Practica 3

----------

Aquí tengo instalado y configurado el Nginx con la opción de IP_Hash:

![Reparto de carga con IP_Hash](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica3/Capturas/carga%20con%20ab%20e%20ip_hash.png?raw=true)

 Estamos repartiendo a Server 2 y el Server 1 que no tiene la sesión no acepta las conexiones.

En la siguiente captura se muestra el **haproxy** con una opción activada para que funcione a varios nucleos:

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica3/Capturas/ab_haproxy_multicore.tiff)

Para la parte **opcional** se pide que se configure otro balanceador. He instalado y configurado **POUND**. 
En la siguiente captura se ve la configuración. De primeras no funcionaba y no conseguía localizar el error. Al final no era un error de configuración, era un simple **error tipográfico**. Como el archivo de configuración tenía un fallo, el balanceador no hacía nada. 

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica3/Capturas/pound%20config%20error%20tipografico.tiff)

Una vez con los tres instalados y configurados. Decidí hacer pruebas de carga con **Apache Benchmark** con cada uno.
Aunque son parecidos en términos de rendimiento, según el entorno en el que se utilicen igual es mejor uno por alguna característica.

Nginx:

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica3/Capturas/tiempos%20nginx.png?raw=true)

HaProxy:

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica3/Capturas/tiempos%20haproxy.tiff)

Pound:

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica3/Capturas/tiempos%20pound.tiff)

Aquí vemos que el más rápido es HaProxy aunque Nginx no da fallos de "Failed Requests". En este segundo caso un usuario podría tener un **retraso en la comunicación** pero no se le cortaría. En el primer caso podrías haber sido uno de los clientes que recibe un **fallo de conexión** por sobrecarga del servidor (en realidad la sobrecarga ha estado en el balanceador).