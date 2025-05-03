import pymysql

def conectar_db():
    try:
        conexion = pymysql.connect(
            host="localhost", 
            user="root",
            password="",
            database="datagronomy",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conexion
    except pymysql.MySQLError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def ejecutar_consulta(consulta, params=None):
    conexion = conectar_db()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                cursor.execute(consulta, params)
                if consulta.strip().upper().startswith("SELECT"):
                    return cursor.fetchall() or []  
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error en consulta: {str(e)}")
            return []  
        finally:
            conexion.close()
    return []  