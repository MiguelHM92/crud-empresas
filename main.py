# Importación de librerías:
import os
from time import sleep
from lib_empresas import *

# Definición de variables iniciales:
cargar_empresas('empresas.txt')
n_opcion = 0

# Definición de cada opción CRUD:
while(n_opcion < 5):
    os.system("clear")
    menu_opciones()
    n_opcion = int(input("INGRESE OPCIÓN : "))
    os.system("clear")
    if n_opcion == 1:
        registrar_empresa()
    elif n_opcion == 2:
        mostrar_empresa()
        input("Presion ENTER para continuar...")
    elif n_opcion == 3:
        actualizar_empresa()
    elif n_opcion == 4:
        eliminar_empresa()
    elif n_opcion == 5:
        grabar_empresas('empresas.txt')
        formato_titulo("[5] SALIR")
    else:
        formato_titulo("OPCIÓN INVÁLIDA!!!")
    sleep(1)
