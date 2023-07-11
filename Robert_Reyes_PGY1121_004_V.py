import datetime

pisos = 10
departamentos_por_piso = 4

precios = {
    'A': 3800,
    'B': 3000,
    'C': 2800,
    'D': 3500
}

disponibles = [[True] * departamentos_por_piso for _ in range(pisos)]
compradores = []

def comprar_departamento():
    piso = int(input("Ingrese el numero del piso (1-10): "))
    tipo = input("Ingrese el tipo de departamento (Use mayusculas)(A, B, C, D): ")
    
    if piso < 1 or piso > pisos or tipo not in precios:
        print("Seleccion invalida")
        return
    
    fila = piso - 1
    columna = ord(tipo) - ord('A')
    
    if disponibles[fila][columna]:
        run = input("Ingrese el RUN del comprador: ")
        compradores.append(run)
        disponibles[fila][columna] = False
        print("Operacion realizada correctamente")
    else:
        print("El departamento seleccionado no esta disponible")

def mostrar_departamentos_disponibles():
    for piso in range(pisos):
        print(f"Piso {piso+1}: ", end="")
        for tipo in precios:
            fila = piso
            columna = ord(tipo) - ord('A')
            estado = 'X' if not disponibles[fila][columna] else ' '
            print(f"{tipo}{piso+1}: {estado} ", end="")
        print()

def ver_listado_compradores():
    compradores_ordenados = sorted(compradores)
    print("Listado de compradores:")
    for comprador in compradores_ordenados:
        print(comprador)

def mostrar_ventas_totales():
    total = sum(precios [tipo] for fila in disponibles for tipo_disponible in fila if tipo_disponible)
    print(f"Ganancias totales: {total} UF")

def salir():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
    print(f"¡Muchas gracias por usar el sistema! | {nombre} {apellido} | Fecha: {fecha_actual}=)")

def menu():
    while True:
        print("---- Menu ----")
        print("1.Comprar departamento")
        print("2.Mostrar departamentos disponibles")
        print("3.Ver listado de compradores")
        print("4.Mostrar ganancias totales")
        print("5.Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            ver_listado_compradores()
        elif opcion == '4':
            mostrar_ventas_totales()
        elif opcion == '5':
            salir()
            break
        else:
            print("Opcion ingresada invalida")

menu()