
from servicios import actualizar_producto, agregar_producto, buscar_producto, calcular_estadisticas, eliminar_producto, mostrar_productos
from Archivos import guardar_csv, cargar_csv
# CRUD es una clase, por tanto cuando importas la clase, no necesitas importar las funiones que estan en ella
# como métodos, en este sentido la linea anterior por eso la comento, cuando requieras guardar o cargar utiliza la clase


from Archivos import CRUD


def integrar_carga(inventario):
    ruta = input("Ruta del archivo CSV a cargar: ")
    datos = cargar_csv(ruta)

    if datos is None:
        return inventario  # No se cambia nada

    print("\n¿Sobrescribir inventario actual? (S/N)")
    decision = input(">>> ").strip().lower()

    if decision == "s":
        print("Inventario reemplazado completamente.")
        return datos

    elif decision == "n":
        print("Fusionando inventarios...")

        nombres_existentes = {p["nombre"]: p for p in inventario}

        for nuevo in datos:
            nombre = nuevo["nombre"]

            if nombre in nombres_existentes:
                # Política recomendada:
                # - Sumar cantidades
                # - Actualizar precio al nuevo
                nombres_existentes[nombre]["cantidad"] += nuevo["cantidad"]
                nombres_existentes[nombre]["precio"] = nuevo["precio"]
            else:
                inventario.append(nuevo)

        print("Fusión completada.")
        return inventario

    else:
        print("Opción inválida. No se realizaron cambios.")
        return inventario


inventario = []

# cuando se utilizar esta funcion como la funcion main, hace falta una linea al final del archivo
# __main__ revisa bien la forma, por eso al final hago llamado a la funcion que estas definiendo

def main_menu():

    while True:
        print("------------------------------------")
        print("-----------MENÚ PRINCIPAL-----------")
        print("1.Agregar producto")
        print("2.Mostrar productos")
        print("3.Buscar producto")
        print("4.Actualizar productos")
        print("5.Eliminar productos")
        print("6.Estadísticas")
        print("7.Guardar CSV")
        print("8.Cargar CSV")
        print("9.Salir")
        print("------------------------------------")

        opcion = input("Elige una opción del Menú (1-9): ")
   
    
        if opcion == "1":
         print(agregar_producto(inventario))

        elif opcion == "2":
         print(mostrar_productos(inventario))

        elif opcion == "3":
         print(buscar_producto(inventario))
        
        elif opcion == "4":
         print(actualizar_producto(inventario))

        elif opcion == "5":
         print(eliminar_producto(inventario))
        
        elif opcion == "6":
         print(calcular_estadisticas(inventario))
        
        elif opcion == "7":
         print(guardar_csv(inventario, incluir_header=True))
         break
        
        elif opcion == "8":
         print(cargar_csv())
         break

        elif opcion == "9":
         print("Gracias por usar nuestra App, feliz día.")
         break

        else:
         print("ERROR: Ingresa un número válido")
        
        
main_menu()  
crud= CRUD()
crud.crear_archivo("archivo.csv")
      

