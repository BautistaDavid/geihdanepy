## GeihdanePy
___

##### **It's time for the GEIH to know python** 

[![PyPI package](https://img.shields.io/badge/pip%20install-geihdanepy-red)](https://pypi.org/project/geihdanepy/) [![License](https://img.shields.io/badge/license-MIT-red)](https://github.com/BautistaDavid/geihdanepy/blob/main/LICENSE)


**Geihdanepy es un paquete de python para facilitar el uso de los datos de la Gran Encuestra Integrada de Hogares del DANE.**

## **Descripción**

El paquete ```geihdanepy``` nace de la idea de estudiantes de economía para facilitar la investigación científica - académica usando los datos de la Gran Encuesta Integrada de Hogares, una de las más importantes bases de datos que proporciona de forma abierta el Departamento Nacional de Estadística **DANE**. 

## **¿Como usar geihdanepy?**

#### Primero lo primero 

Para empezar a trabajar con geihdanepy se debe realizar la instalación del paquete usando el comando ```pip install geihdanepy```. Cuando el paquete este instalado procedemos a importarlo.

```
import geihdanepy as geih
```

## ¡Accedemos a los datos!

Ahora que el paquete está instalado podemos seguir la siguiente sintaxis para solicitar una de las diferentes tablas que ofrece la GEIH.

```
df = geih.datos(2015,'Octubre','Ocupados','Cabecera')
```

Por otro lado, si usted está familiarizado con la GEIH sabrá que esta cuenta principalmente con dos factores de caracterización de los datos aparte de la fecha, los cuales son el módulo y la zona a la que se hace referencia.

De manera que si quiere conocer cómo funciona la sintaxis dentro de  ```geihdanepy``` para hacer referencia los diferentes módulos y zonas puede hacerlo usando las siguientes funciones.

```
geih.info_modulos()   # Acceder a información de los Modulos 
```

```
geih.info_zonas()   # Acceder a información de las zonas  
```

