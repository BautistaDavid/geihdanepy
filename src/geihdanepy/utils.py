def __referenciador_modulo():
    ref_modulo = {'Vivienda':'v',
                   'Caracteristicas':'c',
                   'Fuerza':'f',
                   'Ocupados':'o',
                   'Desocupados':'d',
                   'Inactivos':'i',
                   'Otras actividades':'o_a',
                   'Otros ingresos':'o_i'}
    return ref_modulo 

def __referenciador_modulo_macro2018():
    ref_modulo = {'caracteristicas':'caracteristicas',
        'hogar_vivienda':'hogar_vivienda',
        'fuerza_trabajo':'fuerza_trabajo',
        'migracion':'migracion',
        'no_ocupados':'no_ocupados',
        'ocupados':'ocupados',
        'otras_formas_trabajo':'otras_formas_trabajo',
        'otros ingresos_impuestos':'otros_ingresos_impuestos',
        'tipo_investigacion':'tipo_investigacion'}
    return ref_modulo
    
def __referenciador_zona():
    ref_zona = {'Cabecera':'C',
                "Area":"A",
                "Resto":"R"}
    return ref_zona

def meses():
    return ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']




