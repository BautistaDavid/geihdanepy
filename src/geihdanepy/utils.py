import pandas as pd 

def modulos():
    dic_modules={"Modulos GEIH":["Caracteristicas Generales (personas)",
                                    "Ocupados","Desocupados","Inactivos",
                                    "Fuerza de Trabajo","Otras actividades y ayudas en la semana",
                                    "Otros Ingresos","Vivienda y Hogares"],
                        "Codigo":["c","o","d","i","f","o_a","o_i","v"]}
    dic_modules = pd.DataFrame(dic_modules) 
    dic_modules.set_index("Modulos GEIH",inplace=True)
    return dic_modules


def zonas():
    info_zones={'Zonas GEIH':["Área","Cabecera","Resto"],
                    "Codigo":["A","C","R"]}
    info_zones=pd.DataFrame(info_zones)
    info_zones.set_index("Zonas GEIH",inplace=True)
    return info_zones


def __referenciador_modulo():
    ref_modulo = {'Vivienda':'v',
                   'Caracteristicas':'c',
                   'Fuerza':'f',
                   'Ocupados':'o',
                   'Desocupados':'d',
                   'Inactivos':'i',
                   'Otras Actividades':'o_a',
                   'Otros Ingresos':'o_i'}
    return ref_modulo 

def __referenciador_zona():
    ref_zona = {'Cabecera':'C',
                "Area":"A",
                "Resto":"R"}
    return ref_zona

def meses():
    return ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciemnbre']
