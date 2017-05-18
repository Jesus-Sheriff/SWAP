### Practica 4

----------

En esta práctica lo primero que hay que hacer es activar el acceso por https a una de las máquinas. Para ello hay que crear antes un certificado SSL ( en este caso autofirmado).

Aquí vemos el proceso de activación del SSL.
![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica4/capturas/ACTIVAR_SSL.tiff)

Las claves las hemos generado en la máquina 1 (ubuntu-1) con la orden:

    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache-key -out /etc/apache2/ssl/apache.crt

Creación de las claves:
![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica4/capturas/creacion-de-certificados.tiff)

Aquí se ve el típico error que cometes al escribir mal (puse apache.key y la llave es apache-key):
![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica4/capturas/error_apache.tiff)

Al final nos funciona SSL en la máquina 1:
![enter image description here](https://raw.githubusercontent.com/Jesus-Sheriff/SWAP/master/Practica4/capturas/ssl%20funcionando.tiff)



## Parte opcional

Para configurar la **máquina cortafuegos** externa primero he clonado en VirtualBox el balanceador de carga (máquina LB).
Lo primero que hay que hacer es cambiarle el hostname y asignarle una ip estática nueva.
![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/cambio%20de%20nombre%20de%20host.png?raw=true)

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/ip%20firewall%20antigua.png?raw=true)

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/ip%20firewall%20modificada.png?raw=true)

Aquí ya vemos que el **nombre del host** ha cambiado y la **ip** es la correcta:
![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/maquina%20firewall%20configurado%20nombre%20e%20IP.png?raw=true)

Una vez que tenemos esto se resetea el `iptables` en el servidor 1 (Server 1). En este caso, tenía un script de reseteo de la configuración.
A continuación copio los scripts de iptables de la máquina 1 al firewall por rsync para tener una "plantilla" y modificarla.
![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/copiar%20scripts%20iptables%20a%20firewall.png?raw=true)
Este es el script de configuracion:
![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/script%20firewall%20iptables.png?raw=true)
Script de reseteo:
![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/script%20firewall%20reset.png?raw=true)

Con esto ya podemos ejecutar el script de configuración y comprobar el funcionamiento.
Tengo que destacar un comportamiento extraño que he descubierto.
Resulta que al hacer `ab` sobre el firewall, la máquina queda saturada a los pocos segundos (2 segundos como mucho) y rechaza todos los paquetes hasta un tiempo después. En las siguientes capturas se ve que `ab` funciona al principio, luego se corta e incluso después no funciona `curl`.  Se muestra la salida de `dmesg` junto a `curl`.

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/ab%20empezando.png?raw=true)

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/ab%20bloqueado.png?raw=true)

![enter image description here](https://github.com/Jesus-Sheriff/SWAP/blob/master/Practica4/capturas/dmesg%20sistema%20saturado%20curl%20no%20responde.png?raw=true)

