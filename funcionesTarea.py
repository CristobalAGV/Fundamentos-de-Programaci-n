# Función para calcular los descuentos y el líquido a pagar
def calcular_liquido(sueldo_bruto):
    descuento_salud = sueldo_bruto * 0.07  # 7% de descuento para salud
    descuento_afp = sueldo_bruto * 0.12    # 12% de descuento para AFP
    liquido = sueldo_bruto - (descuento_salud + descuento_afp)
    return descuento_salud, descuento_afp, liquido

# Registar trabajador
def registrar_usuario():
    trabajadores=[]

    nombre=input("Ingrese el nombre del trabajador: ")
    apellido=input("Ingrese el apellido del trabajador: ")
    cargo=input("Ingrese el cargo del trabajador: ")
    salario=float(input("Ingrese el salario del trabajador: "))
    trabajador={"nombre":nombre,"apellido":apellido,"cargo":cargo,"salario":salario}
    trabajadores.append(trabajador)
    print("Usuario ingresado exitosamente.")

# Mostrar lista de trabajador
def mostrar_trabajadores():
    print(f"Listado de trabajadores: {trabajadores}")

# Imprimir planilla de Trabajadores
def planilla():
    with open('planilla.txt','w')as archivo:
        archivo.write("Hola")
