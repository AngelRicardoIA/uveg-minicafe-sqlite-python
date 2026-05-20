import sqlite3

conexion = sqlite3.connect('minicafe.db')
print("Base de datos conectada")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS paquetes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        descripcion TEXT,
        precio REAL
    )
''')
conexion.commit()

conexion.close()