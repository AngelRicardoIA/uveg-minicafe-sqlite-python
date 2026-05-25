import sqlite3
import os

# Crear la base de datos
conexion = sqlite3.connect('minicafe.db')
print("Base de datos conectada")
cursor = conexion.cursor()

#Crear las tablas necesarias para el mini café
def crear_tablas():
    #Tabla paquetes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paquetes (
            id_paquete INTEGER PRIMARY KEY,
            nombre TEXT,
            descripcion TEXT,
            precio REAL
        )
    ''')
    conexion.commit()

    #tabla ventas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id_venta INTEGER PRIMARY KEY,
            fecha TEXT,
            paquete_id INTEGER
        )
    ''')
    conexion.commit()

#Cargar datos iniciales
def cargar_datos_iniciales():
    #Evitar insertar datos duplicados
    cursor.execute('''
        SELECT COUNT(*) FROM paquetes
    ''')
    registros = cursor.fetchone()
    if registros[0] == 0:
        print("No hay registros en la tabla paquetes, insertando datos iniciales...")

        #Insertar datos iniciales en la tabla paquetes
        cursor.execute('''
            INSERT OR IGNORE INTO paquetes (nombre, descripcion, precio) VALUES
            ('Desayunito', 'Huevos, tostadas, café y jugo', 50.0),
            ('Almuercito', 'Pollo a la plancha, arroz y bebida', 80.0),
            ('Ensaladita', 'Ensalada de pollo, sopa y bebida', 60.0),
            ('Comidita', 'Sandwich de pollo, papas fritas y bebida', 70.0),
            ('Postresito', 'Postre del día y malteada', 80.0)
        ''')
        conexion.commit()
    else:
        print("Ya existen registros en la tabla paquetes, no se insertarán datos duplicados.")

#Obtener datos de la tabla paquetes
def mostrar_paquetes():
    cursor.execute('SELECT id_paquete, nombre FROM paquetes')
    paquetes = cursor.fetchall()

    for fila in paquetes:
        id, nombre = fila[0], fila[1]
        print(f"{id} - {nombre}")


def sistema_ventas():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- PAQUETES DISPONIBLES ---")
        mostrar_paquetes()  
        print("\nSi desea regresar al menu principal, escriba 'cancelar'.")
        paquete_id = input("\n¿Qué paquete se ha vendido? (id/cancelar):  ")

        if paquete_id == "cancelar":
            print("Volviendo al menu principal...")
            return
        
        if not paquete_id.isdigit():
            print("Valor invalido, por favor ingrese un número de ID o 'cancelar'.")
            input("Presione Enter para continuar...")
            continue
        
        cursor.execute('''
            SELECT id_paquete FROM paquetes WHERE id_paquete = ?
        ''', (paquete_id,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("ID de paquete no encontrado, por favor intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        cursor.execute('''
            INSERT INTO ventas (fecha, paquete_id) VALUES (date('now'), ?)
        ''', (paquete_id,))
        conexion.commit()
        print("Venta registrada exitosamente")
        input("\nPresione Enter para continuar...")

def reporte_diario():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- REPORTE DIARIO ---")
    cursor.execute('''
        SELECT fecha, nombre
        FROM ventas
                   INNER JOIN paquetes ON ventas.paquete_id = paquetes.id_paquete
        WHERE fecha = date('now')
    ''')
    ventas = cursor.fetchall()
    for venta in ventas:
        fecha, nombre = venta[0], venta[1]
        print(f"{fecha} - {nombre}")

    if not ventas:
        print("No se han registrado ventas para hoy.")
    
def menu_principal():
    salir = False
    while not salir:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n===== MINI CAFE =====")
        print("1. Sistema de ventas")
        print("2. Reporte diario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                sistema_ventas()
            case '2':
                reporte_diario()
                input("\nPresione Enter para continuar...")
            case '3':                
                salir = True
                conexion.close()
            case _:                
                print("Opción no válida, por favor intente de nuevo.")
                input("Presione Enter para continuar...")
                
def main():
    crear_tablas()
    cargar_datos_iniciales()
    menu_principal()

if __name__ == "__main__":    main()
    
