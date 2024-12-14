# Definición de variables a utilizar:
ancho_titulo = 20
dic_empresas = {}

# Definición de las funciones de cargar y grabar información:
def cargar_empresas(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    str_empresas = archivo.read()
    archivo.close()

    lista_empresas = str_empresas.splitlines()
    for str_fila in lista_empresas:
        lista_fila = str_fila.split(',')
        dic_registro = {
           'razon_social':lista_fila[1],
           'direccion' :lista_fila[2]
        }
        dic_nueva_empresa = {
            lista_fila[0] : dic_registro
        }
        dic_empresas.update(dic_nueva_empresa)

def grabar_empresas(nombre_archivo):
    str_empresas = ""
    for empresa_clave, empresa_valor in dic_empresas.items():
        str_empresas += empresa_clave + ","
        for registro_clave, registro_valor in empresa_valor.items():
            str_empresas += registro_valor
            if registro_clave != 'direccion':
                str_empresas += ','
            else:
                str_empresas += '\n'
    
    fsalida = open(nombre_archivo,'w')
    fsalida.write(str_empresas)
    fsalida.close()

# Definición de la función para el formato de titulo y el
# menú de opciones:
def formato_titulo(texto):
    print("~" * ancho_titulo + "~" * ancho_titulo)
    if texto != " ":
        print(" " * 10 + texto)
        print("~" * ancho_titulo + "~" * ancho_titulo)

def menu_opciones():
    formato_titulo("ADMINISTRADOR DE EMPRESAS")
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    formato_titulo(" ")

# Definición de las funciones de las opciones del CRUD:
def registrar_empresa():
    formato_titulo("[1] REGISTRAR EMPRESA")
    ruc = input("Ingrese el RUC de la empresa: ")
    razon_social = input("Ingrese la razón social: ")
    direccion = input("Ingrese la dirección: ")
    dic_nuevo_empresa = {
        ruc : {
            'razon_social': razon_social,
            'direccion': direccion
        }
    }
    dic_empresas.update(dic_nuevo_empresa)

def mostrar_empresa():
    formato_titulo("[2] MOSTRAR EMPRESA")
    for ruc, datos in dic_empresas.items():
        print(f"RUC : {ruc}")
        print(f"Razón Social : {datos['razon_social']}")
        print(f"Dirección : {datos['direccion']}")
        formato_titulo(" ")

def actualizar_empresa():
    formato_titulo("[3] ACTUALIZAR EMPRESA")
    print("Nota: Solo puede actualizar la razón social y la dirección")
    ruc = input("INGRESE EL RUC DE LA EMPRESA A ACTUALIZAR: ")
    if ruc in dic_empresas:
        print(f"EMPRESA A ACTUALIZAR {dic_empresas[ruc]['razon_social']}")
        nuevo_razsocial = input('Razón Social  : ')
        nuevo_direccion = input('Dirección  : ')
        dic_act_empresa = {
            ruc : {
                'razon_social': nuevo_razsocial,
                'direccion': nuevo_direccion
            }
        }
        dic_empresas.update(dic_act_empresa)
        print("LOS DATOS DE LA EMPRESA FUERON ACTUALIZADOS CON EXITO")

def eliminar_empresa():
    formato_titulo("[4] ELIMINAR ALUMNO")
    ruc = input("INGRESE EL RUC DE LA EMPRESA A ELIMINAR: ")
    if ruc in dic_empresas:
        dic_empresas.pop(ruc)
        print("LA EMPRESA FUE ELIMINADA")
    else:
        print("NO SE ENCONTRO EL RUC ESPECIFICADO")

