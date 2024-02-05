empleados = []
i = 1


def agregarEmpleado():

    nombreEmpleado = input('Ingrese el nombre del empleado: ')
    departamentoEmpleado = input("Ingrese el departamento del empleado: ")
    salioEmpleado = float(input("Ingrese el salario del empleado : "))
    empleados.append([i, nombreEmpleado, departamentoEmpleado, salioEmpleado])
    return 1


def verEmpleados():
    global empleados
    for empleado in empleados:
        print(f"Id: {empleado[0]}, Nombre: {empleado[1]}, Departamento: {empleado[2]}, Salario : {empleado[3]}")


def eliminarEmpleado(i):
    verEmpleados()
    idEliminarEmpleado = int(input("Elige el id del empleado que deseas eliminar: "))
    for j in range(len(empleados)):
        if empleados[j][0] == idEliminarEmpleado:
            del empleados[j]
            break


def buscarEmpleado(k):
    idEmpleadoBuscar = int(input("INGRESE EL ID DEL EMPLEADO A BSUCAR : "))
    for k in range(len(empleados)):
        if empleados[k][0] == idEmpleadoBuscar:
            return True
        else:
            return False
        
def salarioPromedio(o):
    global empleados

    for o in range(len(empleados)):

        salarioGeneral = 0
        salarioGeneral += empleados[o][3]

    return (salarioGeneral/len(empleados))

def salarioGeneral(o):
    global empleados

    for o in range(len(empleados)):

        salarioGeneral = 0
        salarioGeneral += empleados[o][3]

    return salarioGeneral


def menu():
    print("""
1. Agregar Empleado
2. Ver Empleado
3. Eliminar Empleado
4. Buscar Empleado
5. Calcular Salario del Promedio
6. Calcular Salario General
. Salir.""")


while True:
    menu()
    opcion = int(input("Elige una Opcion: "))

    if opcion == 1:
        i += agregarEmpleado()
    elif opcion == 2:
        verEmpleados()
    elif opcion == 3:
        eliminarEmpleado(i)
    elif opcion == 4:
        if buscarEmpleado(i) == True:
            print("El empleado fue encontrado")
        else:
            print("El empleado no fue contrado")
    elif opcion == 5:
        print(f"El salario Promedio es: {salarioPromedio(i)}")
    elif opcion == 6:
        print(f"El promedio General es: {salarioGeneral()}")
    else:
        print("ERROR! INGRESE UNA OPCIÓN ENTRE 1-5")
    
    