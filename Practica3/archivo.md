### Practica 3

----------

Aquí tengo instalado y configurado el Nginx con la opción de IP_Hash:

![Reparto de carga con IP_Hash](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica3/Capturas/carga%20con%20ab%20e%20ip_hash.png?raw=true)

 Estamos repartiendo a Server 2 y el Server 1 que no tiene la sesión no acepta las conexiones.

En la siguiente captura se muestra el **haproxy** con una opción activada para que funcione a varios nucleos:

![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica3/Capturas/ab_haproxy_multicore.tiff)

