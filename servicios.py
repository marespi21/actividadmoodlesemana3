
def agregar_producto(inventario):
   
    nombre = input("Ingresa el nombre del producto que quieres agregar: ").strip()

    if not nombre:
        print("Ingresa un nombre, este campo no puede estar vacío.")
        return

    try:
        precio = float(input("Ingresa el precio del nuevo producto: "))
        if precio <= 0:
            print("El precio debe ser mayor a 0, sin puntos, ni comas.")
            return
    except ValueError:
        print("El precio ingresado es inválido. Escribe un número nuevamente.")
        return
    
    try:
        cantidad = int(input("Ingresa la cantidad del nuevo producto: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("La cantidad ingresada es inválida. Debe ser un número entero.")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f"El producto agregado exitosamente{producto}")


def mostrar_productos(inventario):

   print("----INVENTARIO ACTUAL----")
   if not inventario:
        print("El inventario se encuentra vacío.")
        return
    
   for p in inventario:
        print(f"- {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario): 
    nombre = input("Ingresa el nombre del producto que quieres buscar: ").lower()

    for p in inventario:
        if p["nombre"].lower() == nombre:
            print("Producto encontrado:", p)
            return p
    
    print("No hermos encontrado un producto con ese nombre.")
    return None
 


def actualizar_producto(inventario):

   buscar_producto = input("Ingrese el nombre del producto: ")
   if not buscar_producto:
         print("No se ha encontrado el producto.")
         return False
   
   for index, producto in enumerate (inventario): 
      if not isinstance(producto,dict):
         continue
      if producto.get("nombre","").lower() == buscar_producto.lower:
         print("Producto encontrado:", producto)

         actualizado = False
 
         while True:
            print("\n¿Qué quieres actualizar?")
            print("1) Nombre")
            print("2) Precio")
            print("3) Cantidad")
            print("4) Mostrar producto actual")
            print("5) Terminar (volver al menú anterior)")

            opcion = input("Elige una opción (1-5): ").strip()

            if opcion == "1":
               nuevo_nombre = input("Nuevo nombre: ").strip()
               if nuevo_nombre:
                  producto["nombre"] = nuevo_nombre
                  print("✔ Nombre actualizado.")
                  actualizado = True
               else:
                  print("Nombre vacío. No se actualizó.")

            elif opcion == "2":
               nuevo_precio_str = input("Nuevo precio (ej: 12.50): ").strip()
               try:
                  nuevo_precio = float(nuevo_precio_str)
                  if nuevo_precio < 0:
                        raise ValueError("El precio no puede ser negativo.")
                  producto["precio"] = nuevo_precio
                  print("✔ Precio actualizado.")
                  actualizado = True
               except ValueError:
                  print("Error: ingresa un número válido para el precio.")

            elif opcion == "3":
               nueva_cantidad_str = input("Nueva cantidad (entero): ").strip()
               try:
                  nueva_cantidad = int(nueva_cantidad_str)
                  if nueva_cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa.")
                  producto["cantidad"] = nueva_cantidad
                  print("✔ Cantidad actualizada.")
                  actualizado = True
               except ValueError:
                  print("Error: ingresa un entero válido para la cantidad.")

            elif opcion == "4":
               print("\nProducto actual:")
               print(producto)

            elif opcion == "5":
                    # Antes de salir, confirmamos si desea guardar/mostrar resumen
               if actualizado:
                  print("\nActualizaciones guardadas:")
                  print(producto)
               else:
                  print("\nNo se realizaron cambios.")
               return actualizado

            else:
               print("Opción no válida. Elige 1, 2, 3, 4 o 5.")

   print("No se encontró un producto con ese nombre en el inventario.")
   return False


def eliminar_producto(inventario):
   print("-------ELIMINAR PRODUCTO-------")
   nombre = input("Producto a eliminar: ").lower()

   for i, p in enumerate(inventario):
      if p["nombre"].lower() == nombre:
         confirmar = input("¿Estas seguro que deseas eliminar este producto?[si],[no]: ").lower()
         if confirmar == "si":
            inventario.pop(i)
            print("El producto se ha eliminado exitosamente")
         else:
                print("Se ha cancelado la eliminanción del producto.")
         return
    
print("El producto no existe en el inventario.")

def calcular_estadisticas(inventario):
  
   if not inventario:
        print("Inventario vacío.")
        return

   total_unidades = sum(p["cantidad"] for p in inventario)
   total_valor = sum(p["cantidad"] * p["precio"] for p in inventario)
   prod_mas_caro = max(inventario, key=lambda p: p["precio"])
   prod_may_invent = max(inventario, key=lambda p: p["cantidad"])

   print("-------------------------------------------------------------")
   print("\n--- ESTADÍSTICAS ---")
   print("La cantidad total de unidades es:", total_unidades)
   print(f"El valor total del inventario es: ${total_valor:,.2f}")
   print("Producto más costoso es:", prod_mas_caro["nombre"])
   print("El producto con más inventario es:", prod_may_invent["nombre"])
   print("-------------------------------------------------------------")
   

   return calcular_estadisticas