import sqlite3

# Crear la base de datos
conexion = sqlite3.connect('minicafe.db')
print("Base de datos conectada")
cursor = conexion.cursor()

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

conexion.close()