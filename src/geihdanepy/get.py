import pandas as pd 
import urllib
import requests
import collections
from .utils import __referenciador_modulo, __referenciador_zona, meses

def __link(año:int, mes:str, modulo:str, zona:str) -> str:
    """
    Esta funcion esta oculta, contruye el link para acceder a los datos, tambien atrapa errores 
    con respecto al valor de los años, meses. modulos y zonas. 
    """
    mes = mes.capitalize()
    if año not in range(2007,2022):
        print(f'ValueError: {año} no es un año valido.')
        return None
    elif mes not in meses():
        print(f'ValueEror: {mes} no es un mes valido.')
        return None
    modulo, zona = __referenciador_modulo()[modulo.capitalize()],  __referenciador_zona()[zona.capitalize()] 
    return  f'https://raw.githubusercontent.com/BautistaDavid/geihdanepy/main/src/geihdanepy/sets/{año}/{mes}.csv/{zona}{modulo}.csv'


def datos(año:int, mes:str, modulo:str, zona:str) -> pd.DataFrame:
    '''
    Funcion para obtener los datos de la encuesta GEIH del DANE para un
    Area, modulo, mes y año en especifico que se desee.

    ## Parametros
    año: int
        Un año entre el rango de 2007 a 2021, para los cuales actualemente estan
        disponibles los datos de la GEIH.
    mes: str
        El mes de los datos de la GEIH a los que se quieren acceder.
        Ejemplo: ```Abril```
    modulo: str
        El modulo de los datos de la GEIH a los que se quiere acceder, usando la funcion
        ```info_modulos()``` puede acceder a las palabras clave para hacer referencia a cada uno de estos.
        Ejemplo: ```Caracteristicas```
    zona: str
        La zona de los datos de la GEIH a los que se quiere acceder, usando la funcion 
        ```info_zonas()``` puede acceder a las palabras clave para hacer referencia a cada uno de estos.
    
    ## Returns 

    La funcion devuelve un dato tipo ```pd.DataFrame``` con los datos segun los parametros registrados.

    ## Ejemplos

    ```geih.datos('2015', 'Agosto', 'Ocupados', 'Area')``` 
    '''    
    if zona == 'all':
        a = pd.read_csv(__link(año, mes, modulo, 'area'), sep = ';')
        c = pd.read_csv(__link(año, mes, modulo, 'cabecera'), sep = ';') 
        r = pd.read_csv(__link(año, mes, modulo, 'resto'), sep = ';')
        valores = [x for x, y in collections.Counter(list(a.columns) + list(c.columns)).items() if y > 1]  # se queda con las columnas que se repitan en todos los df 
        valores = [x for x, y in collections.Counter(valores + list(r.columns)).items() if y > 1]
        a, c, r = a[valores], c[valores], r[valores]
        return pd.concat([a,c,r])

    else:
        try:
            return pd.read_csv(__link(año, mes, modulo, zona), sep = ';')
        except KeyError as e:
            print(f'KeyError: {e} no se reconoce como un argumento valido')
        except ValueError as e: 
            None   
    

def info_zonas() -> str:
    '''
    Funcion para conocer los codigos de las zonas de la GEIH dentro de las 
    funciones de geihdanepy
    '''
    url = f'https://raw.githubusercontent.com/BautistaDavid/geihdanepy/main/src/geihdanepy/txt_files/zonas.txt'
    file = urllib.request.urlopen(url)
    for line in file:
	    decoded_line = line.decode("utf-8")
	    print(decoded_line)


def info_modulos() ->str:
    '''
    Funcion para conocer los codigos de los modulos de la GEIH dentro de las 
    funciones de geihdanepy
    '''
    url = f'https://raw.githubusercontent.com/BautistaDavid/geihdanepy/main/src/geihdanepy/txt_files/modulos.txt'
    file = urllib.request.urlopen(url)
    for line in file:
	    decoded_line = line.decode("utf-8")
	    print(decoded_line)






