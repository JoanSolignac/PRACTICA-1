productos = []
i = 1

def menu():
    print("1.AGREGAR PRODUCTO\n2.ELIMINAR PRODUCTO\n3.ACTUALIZAR PRODUCTO\n4.BUSCAR PRODUCTO\n5.CALCULAR TOTAL INVENTARIO")

def agregarProdcuto():

    global i
    
    nombreProducto = input("INGRESE EL NOMBRE DEL PRODUCTO : ")
    cantidadProdcuto = int(input("INGRESE LA CANTIDAD DEL PRODUCTO : "))
    while cantidadProdcuto < 0:
        print("ERROR! CANTIDAD NEGATIVA")
        cantidadProdcuto = input("INGRESE LA CANTIDAD DEL PRODUCTO : ")
    precioProducto = float(input("INGRESE EL PRECIO DEL PRODUCTO : "))
    while precioProducto <= 0:
        print("ERROR! PRECIO MENOR O IGUAL A CERO : ")
        precioProducto = float(input("INGRESE EL PRECIO DEL PRODUCTO : "))

    productos.append([id, nombreProducto, cantidadProdcuto, precioProducto])

    return 1

def eliminarProducto():
    global productos
    global i

    print(productos)
    productoEliminar = int(input("INGRESE EL ID DEL PRODCUTO A ELIMINAR : "))

    for j in range(len(productos)):
        if [j][0] == productoEliminar:
            del productoEliminar[j]
            break
    









def main():
    while True:
        menu()
        opcionUsuario = int(input("OPCIÓN = "))
        if opcionUsuario == 1:
            agregarProdcuto(id)
            i += agregarProdcuto()
        elif opcionUsuario == 2:
            eliminarProducto()


    



main()