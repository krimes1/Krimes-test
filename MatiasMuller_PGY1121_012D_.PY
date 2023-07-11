import numpy as np
import click 

def limpiar_pantalla():
    click.clear()

num_pisos = 10
departamentos_por_piso = 4
departamentos = np.zeros((num_pisos, departamentos_por_piso), dtype=int)
lista_clientes = []
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}

def mostrar_departamentos():
    limpiar_pantalla()
    print("Estado actual de los departamentos:\n")
    for piso in range(num_pisos):
        print(f"Piso {piso + 1}: ", end="")
        for departamento in range(departamentos_por_piso):
            if departamentos[piso][departamento] == 0:
                print(f"{chr(65+departamento)}{piso + 1} (⬜︎)", end=" ")
            else:
                print(f"{chr(65+departamento)}{piso + 1} (⛝ )", end=" ")
        print()

def comprar_departamento(piso, tipo_departamento):
    try:
        rut_cliente = int(input("Ingrese el RUT del Cliente\n"))
        lista_clientes.append(rut_cliente)
    except: 
        print("ERROR: TIPO DE RUT INVÁLIDO")
    
    if departamentos[piso][tipo_departamento] == 0:
        departamentos[piso][tipo_departamento] = 1
        limpiar_pantalla()
        print(f"El departamento {chr(65+tipo_departamento)}{piso + 1} ha sido comprado.")
    else:
        print("El departamento ya ha sido vendido.")

def calcular_total_precios():
    total = 0
    for piso in range(num_pisos):
        for departamento in range(departamentos_por_piso):
            if departamentos[piso][departamento] == 1:
                tipo_departamento = chr(65+departamento)
                total += precios[tipo_departamento]
    print(f"Total de precios: {total} UF")



while True:
    print("\n----- Bienvenido a CASA FELÍZ 🏠 -----\n")
    print("1. Mostrar Departamentos Disponibles 🏢")
    print("2. Comprar Departamento 🏢 ")
    print("3. Calcular Total de Precios en UF 💲 ")
    print("4. Cerrar Programa 👋\n")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        mostrar_departamentos()
    elif opcion == "2":
        try:
            piso = int(input(f"Ingrese el número de piso (1-{num_pisos}): ")) - 1

            if piso < 0 or piso >= num_pisos:
                print("ERROR: PISO INVÁLIDO")
                continue
        except:
            print("ERROR: REVISE QUE EL TIPO DE PISO SEA VÁLIDO")
            continue
        tipo_departamento = input("Ingrese el tipo de departamento (A, B, C, D): ").upper()

        if tipo_departamento not in precios:
            print("ERROR: TIPO DE DEPARTAMENTO INVÁLIDO")
            continue

        tipo_index = ord(tipo_departamento) - 65

        comprar_departamento(piso, tipo_index)
    
    elif opcion == "3":
        limpiar_pantalla()
        calcular_total_precios()
    elif opcion == "4":
        limpiar_pantalla()  
        print("Gracias por comprar con CASA FELÍZ, Adiós!")
        print("MatíasMuller_PGY1121_012D")
        print("Fecha: 11-07-2023")
        break
    else:
        print("ERROR: Tipo de Opción Inválida")
