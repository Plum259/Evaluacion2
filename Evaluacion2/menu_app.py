def main():
    compras=[]
    total_gastado=0
    def agregar_compra():
        compras.append(int(input("Ingrese el monto de la compra: ")))
        print("Compra agregada correctamente")
        print(" ")
    def mostrar_compra():
        i=0
        if len(compras) == 0:
            print("No hay compras registradas, por favor registre una primero.")
        else:
            print("compras:")
            while i < len(compras):
                print(f"{i + 1}. ${compras[i]}.00")
                i = i + 1
    def mostrar_total(total_gastado):
        i = 0
        while i < len(compras):
            total_gastado = total_gastado + compras[i]
            i = i+1
        print(f"Total gastado: ${total_gastado}.00")
    while True:
        print("Menú: ")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion=int(input("Seleccione una opcion: "))
        if opcion == 1:
            agregar_compra()
        elif opcion == 2:
            mostrar_compra()
        elif opcion == 3:
            mostrar_total(total_gastado)
        elif opcion == 4:
            print("¡Hasta luego!")
            exit()
        else:
            print("--------------------------")
            print("Ingrese una opcion valida")
            print("--------------------------")
main()
