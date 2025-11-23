import csv
import os

class CRUD:


    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "nombre", "precio", "cantidad"])
            print("Archivo creado.")
        else:
            print("El archivo ya existe.")

    def obtener_id(self, archivo):
        with open(archivo, "r", encoding="utf-8") as file:
            filas = list(csv.reader(file))

        if len(filas) <= 1: 
            return 1

        ultimo_id = int(filas[-1][0])
        return ultimo_id + 1


    def crear(self, archivo, nombre, precio, cantidad):
    
        id_nuevo = self.obtener_id(archivo)
        with open(archivo, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id_nuevo, nombre, precio, cantidad])
        return id_nuevo

    def listar(self, archivo):
        with open(archivo, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  
            return list(reader)


    def guardar_csv(self, inventario, ruta, incluir_header=True):

        if not inventario:
            print("El inventario está vacío. No se puede guardar.")
            return

        try:
            with open(ruta, "w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)

                if incluir_header:
                    writer.writerow(["nombre", "precio", "cantidad"])

                for producto in inventario:
                    writer.writerow([
                        producto["nombre"],
                        producto["precio"],
                        producto["cantidad"]
                    ])

            print(f"Inventario guardado en: {ruta}")

        except PermissionError:
            print("No tienes permiso para escribir en esta ubicación.")

        except Exception as e:
            print(f"Error inesperado: {e}")

    # --------------------------------------
    # Cargar CSV a inventario (lista)
    # --------------------------------------
    def cargar_csv(self, ruta):
        inventario_cargado = []
        filas_invalidas = 0

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                reader = csv.reader(archivo)

                encabezado = next(reader, None)
                encabezado_esperado = ["nombre", "precio", "cantidad"]

                if encabezado != encabezado_esperado:
                    print("✖ Encabezado inválido.")
                    print(f"  Esperado: {encabezado_esperado}")
                    print(f"  Encontrado: {encabezado}")
                    return None

                for fila in reader:
                    if len(fila) != 3:
                        filas_invalidas += 1
                        continue

                    nombre, precio, cantidad = fila

                    try:
                        precio = float(precio)
                        cantidad = int(cantidad)

                        if precio < 0 or cantidad < 0:
                            filas_invalidas += 1
                            continue

                        inventario_cargado.append({
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        })

                    except ValueError:
                        filas_invalidas += 1

        except FileNotFoundError:
            print("Archivo no encontrado.")
            return None

        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

        print(f"Productos cargados: {len(inventario_cargado)}")
        if filas_invalidas:
            print(f"Filas inválidas omitidas: {filas_invalidas}")

        return inventario_cargado
