import tkinter as tk
from views import Login, MenuPrincipal, GestionUsuarios, GestionClientes, GestionLotes, GestionVentas, \
    GestionAlimento, GestionPartos, GestionMontas, GestionGeneral, Crear_Lechon, Crear_Cerda, Crear_Semen
import db_utils  
import hashlib
import tkinter as tk
from tkinter import ttk, messagebox 

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DATAGRONOMY")
        self.geometry("1200x600")
        self.configure(bg="#D3D3D3")

        self.usuario_logueado = None
        self.rol = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Login, MenuPrincipal, GestionUsuarios, GestionClientes, GestionLotes, GestionVentas,
                  GestionAlimento, GestionPartos, GestionMontas, GestionGeneral,
                  Crear_Lechon, Crear_Cerda, Crear_Semen):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_vista(Login)

        conexion = db_utils.conectar_db()
        if conexion:
            print("¡Conexión a la base de datos exitosa!")
            conexion.close()
        else:
            print("No se pudo conectar a la base de datos.")

    def mostrar_vista(self, contenedor):
        if contenedor not in self.frames:
            if contenedor.__name__ not in ["Login", "MenuPrincipal"] and not self.usuario_logueado:
                self.mostrar_vista(Login)
                return
            self.frames[contenedor] = contenedor(self)
        self.frames[contenedor].tkraise()

    def mostrar_vista_con_parametros(self, contenedor, *args):
        frame = contenedor(self, *args)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def verificar_inicio_sesion(self, usuario, contrasena):
        contrasena_hasheada = hashlib.sha256(contrasena.encode()).hexdigest()
        consulta = "SELECT usuario, rol FROM usuarios WHERE Id_usuario = %s AND contrasena = %s"
        params = (usuario, contrasena_hasheada)
        resultado = db_utils.ejecutar_consulta(consulta, params)

        if resultado:
            self.usuario_logueado = resultado[0]['usuario']
            self.rol = resultado[0]['rol']
            print(f"Inicio de sesión exitoso. Usuario: {self.usuario_logueado}, Rol: {self.rol}")
            self.frames[MenuPrincipal] = MenuPrincipal(self, usuario_logueado=self.usuario_logueado, rol=self.rol)
            self.frames[MenuPrincipal].grid(row=0, column=0, sticky="nsew")
            self.mostrar_vista(MenuPrincipal)
        else:
            messagebox.showerror("Error de Inicio de Sesión", "Usuario o contraseña incorrectos.")
    
    def verificar_existencia_usuario(self, numero_documento):
        consulta = "SELECT Id_usuario FROM usuarios WHERE Id_usuario = %s"
        params = (numero_documento,)
        resultado = db_utils.ejecutar_consulta(consulta, params)
        return len(resultado) > 0
    
    def obtener_usuarios(self):
        consulta = "SELECT Id_usuario, nombre, apellido, usuario, rol FROM usuarios"
        try:
            return db_utils.ejecutar_consulta(consulta)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener usuarios: {e}")
            return []

    def insertar_usuario(self, numero_documento, nombre, apellido, usuario, contrasena, rol):
        consulta = "INSERT INTO usuarios (Id_usuario, nombre, apellido, usuario, contrasena, rol) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (numero_documento, nombre, apellido, usuario, contrasena, rol)
        try:
            db_utils.ejecutar_consulta(consulta, params)
        except Exception as e:
            raise Exception(f"Error al insertar usuario: {e}")  
    
    def verificar_existencia_cliente(self, cliente_id):
        consulta = "SELECT Id_cliente FROM clientes WHERE Id_cliente = %s"
        params = (cliente_id,)
        resultado = db_utils.ejecutar_consulta(consulta, params)
        return resultado
    
    def insertar_cliente(self, Id_cliente, nombre, direccion, telefono):
        consulta = "INSERT INTO clientes (Id_cliente, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)"
        params = (Id_cliente, nombre, telefono, direccion)
        try:
            db_utils.ejecutar_consulta(consulta, params)
        except Exception as e:
            raise Exception(f"Error al insertar cliente: {e}")

    def verificar_existencia_lote(self, nombre_lote):
        consulta = "SELECT nombre FROM lotes WHERE nombre = %s"
        params = (nombre_lote,)
        resultado = db_utils.ejecutar_consulta(consulta, params)
        return resultado

    def obtener_lotes(self):
        consulta = "SELECT Id_lote, nombre, descripcion FROM lotes" 
        try:
            return db_utils.ejecutar_consulta(consulta)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener lotes: {e}")
            return []

    def insertar_lote(self, nombre_lote, descripcion_lote):
        consulta = "INSERT INTO lotes (nombre, descripcion) VALUES (%s, %s)"
        params = (nombre_lote, descripcion_lote)
        try:
            db_utils.ejecutar_consulta(consulta, params)
        except Exception as e:
            raise Exception(f"Error al insertar lote: {e}")
        
    def ejecutar_consulta(self, consulta, params=None):
        resultados = db_utils.ejecutar_consulta(consulta, params)
        if resultados is None:
            return []  
        return resultados
    
    def obtener_clientes(self):
        consulta = "SELECT Id_cliente, nombre FROM clientes"
        try:
            return db_utils.ejecutar_consulta(consulta)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener clientes: {e}")
            return []

    def insertar_venta(self, fecha, cantidad_cerdos, cantidad_kilos, precio_kilo, cliente_id):
        consulta = "INSERT INTO ventas (fecha, cant_cerdos, cant_kilos, precio_kilo, Id_cliente) VALUES (%s, %s, %s, %s, %s)"
        params = (fecha, cantidad_cerdos, cantidad_kilos, precio_kilo, cliente_id)
        try:
            db_utils.ejecutar_consulta(consulta, params)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error al insertar venta: {e}")
            return False

    def obtener_ventas(self):
        consulta = "SELECT v.Id_venta, v.fecha, v.cant_cerdos, v.cant_kilos, v.precio_kilo, c.nombre as nombre_cliente FROM ventas v JOIN clientes c ON v.Id_cliente = c.Id_cliente"
        try:
            return db_utils.ejecutar_consulta(consulta)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener ventas: {e}")
            return []

    def obtener_clientes1(self):
        consulta = "SELECT Id_cliente, nombre, direccion, telefono FROM clientes"
        try:
            return db_utils.ejecutar_consulta(consulta)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener clientes: {e}")
            return []

    def insertar_movimiento_alimento(self, tipo_movimiento, cantidad_bultos, tipo_alimento, id_lote):
        consulta = """
        INSERT INTO mov_alimento (tipo_movimiento, cantidad_bultos, tipo_alimento, id_lote, fecha_movimiento)
        VALUES (%s, %s, %s, %s, CURDATE())
        """
        params = (tipo_movimiento, cantidad_bultos, tipo_alimento, id_lote)
        return self.ejecutar_consulta(consulta, params)

    def obtener_stock_alimento(self):
        consulta = """
        SELECT 
            ma.tipo_alimento,
            SUM(CASE WHEN ma.tipo_movimiento = 'Entrada' THEN ma.cantidad_bultos ELSE -ma.cantidad_bultos END) as stock,
            l.nombre as nombre_lote
        FROM mov_alimento ma
        JOIN lotes l ON ma.id_lote = l.Id_lote
        GROUP BY ma.tipo_alimento, ma.id_lote
        """
        try:
            resultados = self.ejecutar_consulta(consulta)
            return resultados if isinstance(resultados, list) else []
        except Exception as e:
            print(f"Error al obtener stock: {e}")
            return []

    def obtener_cerdas(self):
        return self.ejecutar_consulta("SELECT Id_cerda, cod_cerda FROM cerdas")

    def insertar_parto(self, fecha_parto, Id_cerda, Id_lote, nacidos_muertos, cant_machos, cant_hembras, Id_usuario):
        cant_lechones = cant_machos + cant_hembras
        consulta = """
        INSERT INTO partos (
            fecha_parto, Id_cerda, Id_lote, cant_lechones, 
            nacidos_muertos, cant_machos, cant_hembras, Id_usuario
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            fecha_parto, Id_cerda, Id_lote, cant_lechones,
            nacidos_muertos, cant_machos, cant_hembras, Id_usuario
        )
        return self.ejecutar_consulta(consulta, params)

    def obtener_partos(self):
        consulta = """
        SELECT p.Id_parto, p.fecha_parto, c.cod_cerda, l.nombre as lote,
            p.cant_lechones, p.nacidos_muertos, p.cant_machos, p.cant_hembras
        FROM partos p
        JOIN cerdas c ON p.Id_cerda = c.Id_cerda
        JOIN lotes l ON p.Id_lote = l.Id_lote
        """
        return self.ejecutar_consulta(consulta)

    def obtener_cerdas_disponibles(self):
        return self.ejecutar_consulta(
            "SELECT Id_cerda, cod_cerda FROM cerdas WHERE estado IN ('vacia', 'inseminada')"
        )

    def obtener_semen_disponible(self):
        return self.ejecutar_consulta("SELECT Id_semen, cod_semen FROM semen")

    def insertar_monta(self, fecha_monta, Id_cerda, Id_semen, fecha_parto_estimado):
        consulta = """
        INSERT INTO montas (
            fecha_monta, Id_cerda, Id_semen, fecha_parto, Id_usuario
        ) VALUES (%s, %s, %s, %s, %s)
        """
        params = (fecha_monta, Id_cerda, Id_semen, fecha_parto_estimado, self.usuario_logueado)
        return self.ejecutar_consulta(consulta, params)

    def obtener_montas(self):
        consulta = """
        SELECT m.Id_monta, m.fecha_monta, c.cod_cerda, s.cod_semen, 
            m.fecha_parto as fecha_parto_estimado
        FROM montas m
        JOIN cerdas c ON m.Id_cerda = c.Id_cerda
        JOIN semen s ON m.Id_semen = s.Id_semen
        """
        return self.ejecutar_consulta(consulta)

    def actualizar_estado_cerda(self, Id_cerda, nuevo_estado):
        consulta = "UPDATE cerdas SET estado = %s WHERE Id_cerda = %s"
        return self.ejecutar_consulta(consulta, (nuevo_estado, Id_cerda))

    def obtener_cerdas_vacias(self):
        return self.ejecutar_consulta(
            "SELECT Id_cerda, cod_cerda FROM cerdas WHERE estado = 'vacia'"
        )

    def insertar_lechon(self, cod_lechon, fecha_nac, raza, Id_madre, Id_lote):
        consulta = """
        INSERT INTO lechones (cod_lechon, fecha_nac, raza, Id_madre, Id_lote)
        VALUES (%s, %s, %s, %s, %s)
        """
        return self.ejecutar_consulta(consulta, (cod_lechon, fecha_nac, raza, Id_madre, Id_lote))

    def obtener_lechones(self):
        return self.ejecutar_consulta("SELECT * FROM lechones")

    def insertar_cerda(self, cod_cerda, fecha_nac, raza, estado):
        consulta = """
        INSERT INTO cerdas (cod_cerda, fecha_nacimiento, raza, estado)
        VALUES (%s, %s, %s, %s)
        """
        return self.ejecutar_consulta(consulta, (cod_cerda, fecha_nac, raza, estado))

    def obtener_cerdas(self):
        return self.ejecutar_consulta("SELECT * FROM cerdas")

    def insertar_semen(self, cod_semen, fecha_adq, granja, contacto, raza):
        consulta = """
        INSERT INTO semen (cod_semen, fecha_adquisicion, granja_adquisicion, contacto_granja, raza)
        VALUES (%s, %s, %s, %s, %s)
        """
        return self.ejecutar_consulta(consulta, (cod_semen, fecha_adq, granja, contacto, raza))

    def obtener_semen(self):
        return self.ejecutar_consulta("SELECT * FROM semen")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()