datos=[
    {"nombre": "Valentino", "altura": 1.70, "deporte": "voley"},
    {"nombre": "Julian", "altura": 1.95, "deporte": "Basket"},
    {"nombre": "Brian", "altura": 1.80, "deporte": "voley"}
]

def menuPrincipal():
    constancia=True
    while(constancia):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("================== MENÚ PRINCIPAL ==================")
            print("1. Listado")
            print("2. Registro")
            print("3. Agregar")
            print("4. Eliminar")
            print("5. Salir")
            print("====================================================")
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingresa nuevamente")
            elif opcion == 5:
                constancia=False
                print("Gracias por su visita")
                break 
            else:
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 1:
        mostrarListado()
    elif opcion == 2:
        print(opcion)
        registrar()
        
        
def mostrarListado():
    print("==== Listado de personas ====")
    for i, persona in enumerate(datos, start=1):
        print(f"{i}. Nombre: {persona['nombre']}, Altura: {persona['altura']}, Deporte: {persona['deporte']}")            

def registrar():
    nombre = input("Ingrese el nombre: ")
    altura = float(input("Ingrese la altura: "))
    deporte = input("Ingrese el deporte: ")
    datos.append({"nombre": nombre, "altura": altura, "deporte": deporte})
    print("Registro agregado exitosamente.")


menuPrincipal()
