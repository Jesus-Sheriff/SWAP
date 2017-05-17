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

