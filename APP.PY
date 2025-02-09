import pyodbc

# Definir la cadena de conexión
server = 'Eventos.mssql.somee.com'  # Cambia esto con el nombre de tu servidor de Somee
database = 'Eventos'     # Cambia esto con el nombre de tu base de datos
username = 'operaciones_SQLLogin_1'           # Cambia esto con tu usuario de la base de datos
password = '1bfckq7irh'        # Cambia esto con tu contraseña

# Conectar a la base de datos
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejecutar una consulta de prueba
cursor.execute('SELECT * FROM Barrios')  # Asumiendo que tienes la tabla "Barrios"

# Obtener todos los resultados
rows = cursor.fetchall()

# Imprimir los resultados
for row in rows:
    print(f'idBarrio: {row.idBarrio}, Descripcion: {row.Descripcion}, Latitud: {row.Latitud}, Longitud: {row.Longitud}, Cantidad: {row.Cantidad}')

# Cerrar la conexión
conn.close()
