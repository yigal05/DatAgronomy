import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
from datetime import date
import db_utils
from datetime import datetime

class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        tk.Label(self, text="", bg="#D3D3D3").pack(pady=20)

        label_login = tk.Label(self, text="LOG IN", font=("Helvetica", 30, "bold"), bg="#D3D3D3", fg="black")
        label_login.pack(pady=20)

        frame_usuario = tk.Frame(self, bg="#D3D3D3")
        frame_usuario.pack(pady=10)
        tk.Label(frame_usuario, text="USUARIO:", font=("Helvetica", 18), bg="#D3D3D3", fg="black").pack(side="left", padx=10)
        self.entrada_usuario = tk.Entry(frame_usuario, font=("Helvetica", 14), width=30)
        self.entrada_usuario.pack(side="left")

        frame_contrasena = tk.Frame(self, bg="#D3D3D3")
        frame_contrasena.pack(pady=10)
        tk.Label(frame_contrasena, text="CONTRASEÑA:", font=("Helvetica", 18), bg="#D3D3D3", fg="black").pack(side="left", padx=10)
        self.entrada_contrasena = tk.Entry(frame_contrasena, font=("Helvetica", 14), width=30, show="*")
        self.entrada_contrasena.pack(side="left")

        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=30)

        boton_login = tk.Button(frame_botones, text="INGRESAR", bg="#E6A9D3", font=("Helvetica", 16, "bold"),
                           command=self.login)
        boton_login.pack(side="left", padx=20)

    def login(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        self.master.verificar_inicio_sesion(usuario, contrasena)


class TablaGeneral(tk.Frame):
    def __init__(self, master, titulo, consulta):
        super().__init__(master, bg="#D3D3D3")

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16),
                                 bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)

        label_titulo = tk.Label(barra_superior, text=titulo, font=("Helvetica", 20, "bold"),
                                bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        contenedor = tk.Frame(self, bg="#D3D3D3")
        contenedor.pack(expand=True)

        label_tabla = tk.Label(contenedor, text=f"Aquí se mostraría una consulta: {consulta}",
                               font=("Helvetica", 18), bg="#D3D3D3")
        label_tabla.pack(pady=50)


class MenuPrincipal(tk.Frame):
    def __init__(self, master, usuario_logueado="", rol=""):
        super().__init__(master, bg="#D3D3D3")
        self.rol = rol
        self.usuario_logueado = usuario_logueado

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                 font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        label_usuario = tk.Label(self, text=f"USUARIO: {self.usuario_logueado.upper()}",
                                  font=("Helvetica", 12), bg="#D3D3D3", fg="black")
        label_usuario.pack(pady=10)

        contenedor_botones = tk.Frame(self, bg="#D3D3D3")
        contenedor_botones.pack(expand=True)
        nombres_botones = list()

        if self.rol == "administrador":
            nombres_botones = [
                ("GESTIÓN USUARIOS", lambda: master.mostrar_vista(GestionUsuarios)),
                ("GESTIÓN CLIENTES", lambda: master.mostrar_vista(GestionClientes)),
                ("GESTIÓN LOTES", lambda: master.mostrar_vista(GestionLotes)),
                ("GESTIÓN VENTAS", lambda: master.mostrar_vista(GestionVentas)),
                ("GESTIÓN ALIMENTO", lambda: master.mostrar_vista(GestionAlimento)),
                ("GESTIÓN PARTOS", lambda: master.mostrar_vista(GestionPartos)),
                ("GESTIÓN MONTAS", lambda: master.mostrar_vista(GestionMontas)),
                ("GESTIÓN ANIMALES", lambda: master.mostrar_vista(GestionGeneral))
            ]
        elif self.rol == "granjero":
            nombres_botones = [
                ("GESTIÓN ALIMENTO", lambda: master.mostrar_vista(GestionAlimento)),
                ("GESTIÓN PARTOS", lambda: master.mostrar_vista(GestionPartos)),
                ("GESTIÓN MONTAS", lambda: master.mostrar_vista(GestionMontas)),
                ("GESTIÓN ANIMALES", lambda: master.mostrar_vista(GestionGeneral))
            ]
        else:
            nombres_botones = [("SALIR", None)]

        filas = 2
        columnas = 4
        indice = 0
        for fila in range(filas):
            for columna in range(columnas):
                if indice < len(nombres_botones):
                    texto, comando = nombres_botones[indice]
                    boton = tk.Button(contenedor_botones, text=texto,
                                        font=("Helvetica", 14, "bold"), bg="#E6A9D3",
                                        width=18, height=6,
                                        command=comando if comando else None)
                    boton.grid(row=fila, column=columna, padx=20, pady=20, sticky="nsew")
                    indice += 1

        for i in range(columnas):
            contenedor_botones.grid_columnconfigure(i, weight=1)
        for i in range(filas):
            contenedor_botones.grid_rowconfigure(i, weight=1)


class GestionUsuarios(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                 font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=30)

        campos = [
            "Número de documento:", "Nombre:", "Apellido:",
            "Contraseña", "Confirmar contraseña:", "Rol:"
        ]

        self.entradas = {}

        for idx, campo in enumerate(campos):
            label = tk.Label(contenedor_formulario, text=campo, font=("Helvetica", 14), bg="#D3D3D3", fg="black")
            label.grid(row=idx, column=0, sticky="e", padx=10, pady=5)

            if campo == "Rol:":
                entrada = ttk.Combobox(contenedor_formulario, values=["Granjero", "Administrador"], font=("Helvetica", 14))
                entrada.current(0)
            else:
                entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 14))
                if "Contraseña" in campo:
                    entrada.config(show="*")

            entrada.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entrada

        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)

        boton_crear = tk.Button(frame_botones, text="CREAR USUARIO", bg="#E6A9D3",
                                 font=("Helvetica", 16, "bold"), command=self.crear_usuario)
        boton_crear.pack(side="left", padx=20)

        boton_ver = tk.Button(frame_botones, text="Ver usuarios...", bg="#E6A9D3",
                                 font=("Helvetica", 16, "bold"), command=self.ver_usuarios)
        boton_ver.pack(side="left", padx=20)

    def crear_usuario(self):
        numero_documento = self.entradas["Número de documento:"].get()
        nombre = self.entradas["Nombre:"].get()
        apellido = self.entradas["Apellido:"].get()
        contrasena = self.entradas["Contraseña"].get()
        confirmar_contrasena = self.entradas["Confirmar contraseña:"].get()
        rol = self.entradas["Rol:"].get()

        if not all([numero_documento, nombre, apellido, contrasena, confirmar_contrasena, rol]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if contrasena != confirmar_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        usuario = nombre.lower() + "." + apellido.lower()
        contrasena_hasheada = hashlib.sha256(contrasena.encode()).hexdigest()

        if self.master.verificar_existencia_usuario(numero_documento):
            messagebox.showerror("Error", "Ya existe un usuario con este número de documento.")
            return

        try:
            self.master.insertar_usuario(numero_documento, nombre, apellido, usuario, contrasena_hasheada, rol)
            messagebox.showinfo("Éxito", "Usuario creado correctamente.")
            self.limpiar_entradas() 
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el usuario: {e}")

    def limpiar_entradas(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)

    # En la clase GestionUsuarios, modificar el método ver_usuarios:
    def ver_usuarios(self):
        usuarios = self.master.obtener_usuarios()
        if usuarios:
            ventana_usuarios = tk.Toplevel(self.master)
            ventana_usuarios.title("Usuarios Registrados")

            frame_tabla = tk.Frame(ventana_usuarios)
            frame_tabla.pack(fill="both", expand=True)
            
            frame_botones = tk.Frame(ventana_usuarios)
            frame_botones.pack(fill="x", pady=5)

            tree = ttk.Treeview(frame_tabla, columns=("Número de Documento", "Nombre", "Apellido", "Usuario", "Rol"), show="headings")
            tree.heading("Número de Documento", text="Número de Documento")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Apellido", text="Apellido")
            tree.heading("Usuario", text="Usuario")
            tree.heading("Rol", text="Rol")
            
            scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            for usuario in usuarios:
                tree.insert("", tk.END, values=(
                    usuario['Id_usuario'],
                    usuario['nombre'],
                    usuario['apellido'],
                    usuario['usuario'],
                    usuario['rol']
                ))

            # Botón Eliminar
            btn_eliminar = tk.Button(frame_botones, text="Eliminar selección", bg="#ff6b6b", fg="white",
                                command=lambda: self.eliminar_usuario_seleccionado(tree, ventana_usuarios))
            btn_eliminar.pack(side="right", padx=5)
        else:
            messagebox.showinfo("Información", "No hay usuarios registrados.")

    def eliminar_usuario_seleccionado(self, tree, ventana):
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario para eliminar.")
            return
        
        id_usuario = tree.item(seleccion[0])['values'][0]
        
        if messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este usuario?"):
            try:
                consulta = "DELETE FROM usuarios WHERE Id_usuario = %s"
                if self.master.ejecutar_consulta(consulta, (id_usuario,)):
                    messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                    tree.delete(seleccion)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el usuario.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar usuario: {e}")


class GestionClientes(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")

        # Barra azul superior
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        # Botón volver (flecha)
        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                 font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        # Formulario
        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=30)

        campos = ["Id:", "Nombre:", "Dirección:", "Teléfono:"]
        self.entradas = {}

        for idx, campo in enumerate(campos):
            label = tk.Label(contenedor_formulario, text=campo, font=("Helvetica", 14), bg="#D3D3D3", fg="black")
            label.grid(row=idx, column=0, sticky="e", padx=10, pady=5)
            entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 14))
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entrada

        # Botones
        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)

        boton_crear = tk.Button(frame_botones, text="CREAR CLIENTE", bg="#E6A9D3",
                                 font=("Helvetica", 16, "bold"), command=self.crear_cliente)
        boton_crear.pack(side="left", padx=20)

        boton_ver = tk.Button(frame_botones, text="Ver clientes...", bg="#E6A9D3",
                                 font=("Helvetica", 16, "bold"), command=self.ver_clientes)
        boton_ver.pack(side="left", padx=20)

    def crear_cliente(self):
        Id = self.entradas["Id:"].get()
        nombre = self.entradas["Nombre:"].get()
        telefono = self.entradas["Teléfono:"].get()
        direccion = self.entradas["Dirección:"].get()

        if not all([Id, nombre, direccion, telefono]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            resultado = self.master.verificar_existencia_cliente(Id)
            if len(resultado) > 0:
                messagebox.showerror("Error", "Ya existe un cliente con este ID.")
                return
            self.master.insertar_cliente(Id, nombre, direccion, telefono)
            messagebox.showinfo("Éxito", "Cliente creado correctamente.")
            self.limpiar_entradas()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el cliente: {e}")

    # En la clase GestionClientes, modificar el método ver_clientes:
    def ver_clientes(self):
        clientes = self.master.obtener_clientes1()
        if clientes:
            ventana_clientes = tk.Toplevel(self.master)
            ventana_clientes.title("Clientes Registrados")

            frame_tabla = tk.Frame(ventana_clientes)
            frame_tabla.pack(fill="both", expand=True)
            
            frame_botones = tk.Frame(ventana_clientes)
            frame_botones.pack(fill="x", pady=5)

            tree = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Dirección", "Teléfono"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Dirección", text="Dirección")
            tree.heading("Teléfono", text="Teléfono")
            
            scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            for cliente in clientes:
                tree.insert("", tk.END, values=(cliente['Id_cliente'], cliente['nombre'], cliente['direccion'], cliente['telefono']))

            # Botón Eliminar
            btn_eliminar = tk.Button(frame_botones, text="Eliminar selección", bg="#ff6b6b", fg="white",
                                command=lambda: self.eliminar_cliente_seleccionado(tree, ventana_clientes))
            btn_eliminar.pack(side="right", padx=5)
        else:
            messagebox.showinfo("Información", "No hay clientes registrados.")

    def eliminar_cliente_seleccionado(self, tree, ventana):
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un cliente para eliminar.")
            return
        
        id_cliente = tree.item(seleccion[0])['values'][0]
        
        if messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este cliente?"):
            try:
                consulta = "DELETE FROM clientes WHERE Id_cliente = %s"
                if self.master.ejecutar_consulta(consulta, (id_cliente,)):
                    messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                    tree.delete(seleccion)
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el cliente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar cliente: {e}")

    def limpiar_entradas(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)


class GestionLotes(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                 font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=30)

        campos = ["Nombre:", "Descripción:"]
        self.entradas = {}

        for idx, campo in enumerate(campos):
            label = tk.Label(contenedor_formulario, text=campo, font=("Helvetica", 14), bg="#D3D3D3", fg="black")
            label.grid(row=idx, column=0, sticky="e", padx=10, pady=5)
            entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 14))
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entrada

        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)

        boton_crear = tk.Button(frame_botones, text="CREAR LOTE", bg="#E6A9D3",
                                 font=("Helvetica", 16, "bold"), command=self.crear_lote)
        boton_crear.pack(side="left", padx=20)

        boton_ver = tk.Button(frame_botones, text="Ver Lotes...", bg="#E6A9D3",
                                 font=("Helvetica", 16, "bold"), command=self.ver_lotes)
        boton_ver.pack(side="left", padx=20)

    def crear_lote(self):
        nombre_lote = self.entradas["Nombre:"].get()
        descripcion_lote = self.entradas["Descripción:"].get()

        if not all([nombre_lote, descripcion_lote]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            resultado = self.master.verificar_existencia_lote(nombre_lote)
            if resultado:
                messagebox.showerror("Error", "Ya existe un lote con este nombre.")
                return
            self.master.insertar_lote(nombre_lote, descripcion_lote)
            messagebox.showinfo("Éxito", "Lote creado correctamente.")
            self.limpiar_entradas()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el lote: {e}")

    def limpiar_entradas(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)

    def ver_lotes(self):
        lotes = self.master.obtener_lotes() 
        if lotes:
            ventana_lotes = tk.Toplevel(self.master)
            ventana_lotes.title("Lotes Registrados")

            tree = ttk.Treeview(ventana_lotes, columns=("ID", "Nombre", "Descripción"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Descripción", text="Descripción")
            tree.pack(expand=True, fill="both")

            for lote in lotes:
                tree.insert("", tk.END, values=(lote['Id_lote'], lote['nombre'], lote['descripcion']))
        else:
            messagebox.showinfo("Información", "No hay lotes registrados.")


class GestionVentas(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                 font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=30)

        campos = [
            "Fecha:", "Cantidad Cerdos:", "Cantidad Kilos", "Precio Kilo:", "Cliente:" 
        ]
        self.entradas = {}

        for idx, campo in enumerate(campos):
            label = tk.Label(contenedor_formulario, text=campo, font=("Helvetica", 14), bg="#D3D3D3", fg="black")
            label.grid(row=idx, column=0, sticky="e", padx=10, pady=5)
            if campo == "Cliente:":
                clientes = self.master.obtener_clientes()
                nombres_clientes = [cliente['nombre'] for cliente in clientes]
                self.combo_cliente = ttk.Combobox(contenedor_formulario, values=nombres_clientes, font=("Helvetica", 14))
                self.combo_cliente.grid(row=idx, column=1, padx=10, pady=5)
            else:
                entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 14))
                entrada.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = entrada

        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)

        boton_generar = tk.Button(frame_botones, text="CREAR VENTA", bg="#E6A9D3",
                                    font=("Helvetica", 16, "bold"), command=self.crear_venta)
        boton_generar.pack(side="left", padx=20)

        boton_ver = tk.Button(frame_botones, text="Ver Ventas...", bg="#E6A9D3",
                                font=("Helvetica", 16, "bold"),
                                command=self.ver_ventas)
        boton_ver.pack(side="left", padx=20)

    def crear_venta(self):
        fecha = date.today()
        cantidad_cerdos = self.entradas["Cantidad Cerdos:"].get()
        cantidad_kilos = self.entradas["Cantidad Kilos"].get()
        precio_kilo = self.entradas["Precio Kilo:"].get()
        nombre_cliente = self.combo_cliente.get()

        if not all([cantidad_cerdos, cantidad_kilos, precio_kilo, nombre_cliente]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            cantidad_cerdos = int(cantidad_cerdos)
            cantidad_kilos = float(cantidad_kilos)
            precio_kilo = float(precio_kilo)

            if cantidad_cerdos <= 0 or cantidad_kilos <= 0 or precio_kilo <= 0:
                messagebox.showerror("Error", "Los valores deben ser mayores a cero.")
                return

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos (ej: 10, 5.5).")
            return

        # Resto del código (insertar en la base de datos)
        clientes = self.master.obtener_clientes()
        cliente_seleccionado = next((cliente for cliente in clientes if cliente['nombre'] == nombre_cliente), None)
        
        if not cliente_seleccionado:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return

        cliente_id = cliente_seleccionado['Id_cliente']

        if self.master.insertar_venta(fecha, cantidad_cerdos, cantidad_kilos, precio_kilo, cliente_id):
            messagebox.showinfo("Éxito", "Venta registrada correctamente.")
            self.limpiar_entradas()
        else:
            messagebox.showerror("Error", "No se pudo registrar la venta.")

    def ver_ventas(self):
        ventas = self.master.obtener_ventas()
        if ventas:
            ventana_ventas = tk.Toplevel(self.master)
            ventana_ventas.title("Ventas Registradas")

            tree = ttk.Treeview(ventana_ventas, columns=("ID Venta", "Fecha", "Cantidad Cerdos", "Cantidad Kilos", "Precio Kilo", "Cliente"), show="headings")
            tree.heading("ID Venta", text="ID Venta")
            tree.heading("Fecha", text="Fecha")
            tree.heading("Cantidad Cerdos", text="Cantidad Cerdos")
            tree.heading("Cantidad Kilos", text="Cantidad Kilos")
            tree.heading("Precio Kilo", text="Precio Kilo")
            tree.heading("Cliente", text="Cliente")
            tree.pack(expand=True, fill="both")

            for venta in ventas:
                tree.insert("", tk.END, values=(venta['Id_venta'], venta['fecha'], venta['cant_cerdos'], venta['cant_kilos'], venta['precio_kilo'], venta['nombre_cliente']))
        else:
            messagebox.showinfo("Información", "No hay ventas registradas.")

    def limpiar_entradas(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.combo_cliente.set("")


class GestionAlimento(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        self.lotes = self.master.obtener_lotes()

        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")

        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16),
                                 bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(
                                     MenuPrincipal, master.usuario_logueado, master.rol),
                                 borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)

        label_titulo = tk.Label(barra_superior, text="D A T A G R O N O M Y",
                                 font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        self.contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        self.contenedor_formulario.pack(pady=30)

        campos = [
            "Tipo movimiento:", "Cantidad de bultos:", "Tipo de alimento:",
            "Lote:"
        ]
        
        self.valores_compbox = ["preiniciador", "iniciacion", "levante", "engorde",
                                 "finalizador", "gestacion", "lactancia"]

        self.entradas = {}
        self.crear_formulario(campos)

        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)

        boton_registrar = tk.Button(frame_botones, text="REGISTRAR MOVIMIENTO", bg="#E6A9D3",
                                    font=("Helvetica", 16, "bold"), command=self.registrar_movimiento)
        boton_registrar.pack(side="left", padx=20)

        boton_ver_stock = tk.Button(frame_botones, text="VER STOCK", bg="#E6A9D3",
                                     font=("Helvetica", 16, "bold"), command=self.ver_stock)
        boton_ver_stock.pack(side="left", padx=20)

    def crear_formulario(self, campos):
        for idx, campo in enumerate(campos):
            label = tk.Label(self.contenedor_formulario, text=campo,
                             font=("Helvetica", 14), bg="#D3D3D3", fg="black")
            label.grid(row=idx, column=0, sticky="e", padx=10, pady=5)

            if campo == "Tipo movimiento:":
                self.combo_tipo_movimiento = ttk.Combobox(self.contenedor_formulario,
                                     values=["Entrada", "Salida"],
                                     font=("Helvetica", 14))
                self.combo_tipo_movimiento.current(0)
                self.combo_tipo_movimiento.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = self.combo_tipo_movimiento 
            elif campo == "Tipo de alimento:":
                self.combo_tipo_alimento = ttk.Combobox(self.contenedor_formulario,
                                     values=self.valores_compbox,
                                     font=("Helvetica", 14))
                self.combo_tipo_alimento.current(0)
                self.combo_tipo_alimento.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = self.combo_tipo_alimento 
            elif campo == "Lote:":
                self.lotes = self.obtener_nombres_lotes()
                nombres_lotes = [lote["nombre"] for lote in self.lotes]
                self.combo_lote = ttk.Combobox(self.contenedor_formulario,
                                             values=nombres_lotes,
                                             font=("Helvetica", 14))
                self.combo_lote.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = self.combo_lote  
            else:
                entrada = tk.Entry(self.contenedor_formulario,
                                 font=("Helvetica", 14))
                entrada.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = entrada  

    def obtener_nombres_lotes(self):
        try:
            lotes = self.master.obtener_lotes()
            return lotes if lotes else []
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener los lotes: {e}")
            return []

    def registrar_movimiento(self):
        tipo_movimiento = self.combo_tipo_movimiento.get()
        cantidad_bultos = self.entradas["Cantidad de bultos:"].get()
        tipo_alimento = self.combo_tipo_alimento.get()
        nombre_lote = self.combo_lote.get()
        
        if not cantidad_bultos.isdigit():
            messagebox.showerror("Error", "Cantidad de bultos debe ser un número.")
            return
        
        id_lote = next((lote["Id_lote"] for lote in self.lotes if lote["nombre"] == nombre_lote), None)
        if not id_lote:
            messagebox.showerror("Error", "Lote no válido.")
            return
        
        if self.master.insertar_movimiento_alimento(tipo_movimiento, int(cantidad_bultos), tipo_alimento, id_lote):
            messagebox.showinfo("Éxito", "Movimiento registrado.")
            self.limpiar_entradas()

    def limpiar_entradas(self):
        for entrada in self.entradas.values():
            if isinstance(entrada, ttk.Combobox):
                entrada.set('')
            else:
                entrada.delete(0, tk.END)

    def ver_stock(self):
        stock = self.master.obtener_stock_alimento()
        
        if not stock or not isinstance(stock, list):
            messagebox.showinfo("Info", "No hay datos de stock o hubo un error.")
            return
        
        ventana = tk.Toplevel(self)
        ventana.title("Stock de Alimento")
        
        tree = ttk.Treeview(ventana, columns=("Tipo", "Stock", "Lote"), show="headings")
        tree.heading("Tipo", text="Tipo de Alimento")
        tree.heading("Stock", text="Stock (Bultos)")
        tree.heading("Lote", text="Ubicación (Lote)")
        
        for item in stock:
            tree.insert("", tk.END, values=(item["tipo_alimento"], item["stock"], item["nombre_lote"]))
        
        tree.pack(expand=True, fill="both")


class GestionPartos(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")
        
        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16),
                                 bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(
                                     MenuPrincipal, master.usuario_logueado, master.rol),
                                 borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)
        
        tk.Label(
            barra_superior, text="GESTIÓN DE PARTOS", font=("Helvetica", 20, "bold"), 
            bg="#316A99", fg="black"
        ).pack(pady=5)
        
        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=20)
        
        campos = [
            "Fecha de parto (YYYY-MM-DD):", "Cerda:", "Lote:", 
            "Nacidos muertos:", "Machos:", "Hembras:"
        ]
        self.entradas = {}
        
        for idx, campo in enumerate(campos):
            tk.Label(
                contenedor_formulario, text=campo, font=("Helvetica", 12), 
                bg="#D3D3D3", fg="black"
            ).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            
            if campo == "Cerda:":
                self.combo_cerda = ttk.Combobox(contenedor_formulario, font=("Helvetica", 12), state="readonly")
                self.combo_cerda.grid(row=idx, column=1, padx=10, pady=5)
                self.cargar_cerdas()
            elif campo == "Lote:":
                self.combo_lote = ttk.Combobox(contenedor_formulario, font=("Helvetica", 12), state="readonly")
                self.combo_lote.grid(row=idx, column=1, padx=10, pady=5)
                self.cargar_lotes()
            else:
                entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 12))
                entrada.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = entrada
        
        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones, text="Registrar Parto", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.registrar_parto
        ).pack(side="left", padx=20)
        
        tk.Button(
            frame_botones, text="Ver Partos Registrados", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.ver_partos
        ).pack(side="left", padx=20)
    
    def cargar_cerdas(self):
        cerdas = self.master.obtener_cerdas()
        if cerdas:
            self.combo_cerda["values"] = [f"{cerda['cod_cerda']} (ID: {cerda['Id_cerda']})" for cerda in cerdas]
        else:
            messagebox.showwarning("Advertencia", "No hay cerdas registradas.")
    
    def cargar_lotes(self):
        lotes = self.master.obtener_lotes()
        if lotes:
            self.combo_lote["values"] = [f"{lote['nombre']} (ID: {lote['Id_lote']})" for lote in lotes]
        else:
            messagebox.showwarning("Advertencia", "No hay lotes registrados.")
    
    def registrar_parto(self):
        fecha_parto = self.entradas["Fecha de parto (YYYY-MM-DD):"].get()
        cerda_texto = self.combo_cerda.get()
        lote_texto = self.combo_lote.get()
        nacidos_muertos = self.entradas["Nacidos muertos:"].get()
        machos = self.entradas["Machos:"].get()
        hembras = self.entradas["Hembras:"].get()
        Id_usuario = self.master.usuario_logueado

        if not all([fecha_parto, cerda_texto, lote_texto, machos, hembras]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            Id_cerda = int(cerda_texto.split("ID: ")[1].replace(")", ""))
            Id_lote = int(lote_texto.split("ID: ")[1].replace(")", ""))
            nacidos_muertos = int(nacidos_muertos) if nacidos_muertos else 0
            machos = int(machos)
            hembras = int(hembras)

            if machos < 0 or hembras < 0:
                raise ValueError("Los valores deben ser positivos.")

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
            return

        if self.master.insertar_parto(
            fecha_parto, Id_cerda, Id_lote, nacidos_muertos, machos, hembras, Id_usuario
        ):
            messagebox.showinfo("Éxito", "Parto registrado correctamente.")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo registrar el parto.")
    
    def ver_partos(self):
        partos = self.master.obtener_partos()
        if not partos:
            messagebox.showinfo("Info", "No hay partos registrados.")
            return
        
        ventana = tk.Toplevel(self)
        ventana.title("Partos Registrados")
        
        columnas = ("ID", "Fecha", "Cerda", "Lote", "Total", "Muertos", "Machos", "Hembras")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        
        for parto in partos:
            tree.insert("", tk.END, values=(
                parto["Id_parto"],
                parto["fecha_parto"],
                parto["cod_cerda"],
                parto["lote"],
                parto["cant_lechones"],
                parto["nacidos_muertos"],
                parto["cant_machos"],
                parto["cant_hembras"]
            ))
        
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        tree.pack(expand=True, fill="both")
    
    def limpiar_formulario(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.combo_cerda.set("")
        self.combo_lote.set("")


class GestionMontas(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")
        
        boton_volver = tk.Button(
            barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
            command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol)
        )
        boton_volver.pack(side="left", padx=10, pady=5)
        
        tk.Label(
            barra_superior, text="GESTIÓN DE MONTAS", font=("Helvetica", 20, "bold"), 
            bg="#316A99", fg="black"
        ).pack(pady=5)
        
        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=20)
        
        campos = [
            "Fecha de monta (YYYY-MM-DD):", "Cerda:", "Semen:", 
            "Fecha estimada de parto (YYYY-MM-DD):"
        ]
        self.entradas = {}
        
        for idx, campo in enumerate(campos):
            tk.Label(
                contenedor_formulario, text=campo, font=("Helvetica", 12), 
                bg="#D3D3D3", fg="black"
            ).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            
            if campo == "Cerda:":
                self.combo_cerda = ttk.Combobox(contenedor_formulario, font=("Helvetica", 12), state="readonly")
                self.combo_cerda.grid(row=idx, column=1, padx=10, pady=5)
                self.combo_cerda.bind("<Button-1>", lambda e: self.cargar_cerdas())
            elif campo == "Semen:":
                self.combo_semen = ttk.Combobox(contenedor_formulario, font=("Helvetica", 12), state="readonly")
                self.combo_semen.grid(row=idx, column=1, padx=10, pady=5)
                self.cargar_semen()
            else:
                entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 12))
                entrada.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = entrada
        
        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones, text="Registrar Monta", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.registrar_monta
        ).pack(side="left", padx=20)
        
        tk.Button(
            frame_botones, text="Ver Montas Registradas", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.ver_montas
        ).pack(side="left", padx=20)
    
    def cargar_cerdas(self):
        cerdas = self.master.obtener_cerdas_vacias()
        if cerdas:
            self.combo_cerda["values"] = [f"{cerda['cod_cerda']} (ID: {cerda['Id_cerda']})" for cerda in cerdas]
        else:
            messagebox.showwarning("Advertencia", "No hay cerdas vacías disponibles.", parent=self)
    
    def cargar_semen(self):
        semen = self.master.obtener_semen_disponible()
        if semen:
            self.combo_semen["values"] = [f"{s['cod_semen']} (ID: {s['Id_semen']})" for s in semen]
    
    def registrar_monta(self):
        fecha_monta = self.entradas["Fecha de monta (YYYY-MM-DD):"].get()
        cerda_texto = self.combo_cerda.get()
        semen_texto = self.combo_semen.get()
        fecha_parto_estimado = self.entradas["Fecha estimada de parto (YYYY-MM-DD):"].get()
        
        if not all([fecha_monta, cerda_texto, semen_texto, fecha_parto_estimado]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            Id_cerda = int(cerda_texto.split("ID: ")[1].replace(")", ""))
            Id_semen = int(semen_texto.split("ID: ")[1].replace(")", ""))
            fecha_monta_dt = datetime.strptime(fecha_monta, "%Y-%m-%d").date()
            fecha_parto_dt = datetime.strptime(fecha_parto_estimado, "%Y-%m-%d").date()
            
            if fecha_parto_dt <= fecha_monta_dt:
                raise ValueError("La fecha de parto debe ser posterior a la monta.")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Dato inválido: {str(e)}")
            return
        
        if self.master.insertar_monta(fecha_monta, Id_cerda, Id_semen, fecha_parto_estimado):
            messagebox.showinfo("Éxito", "Monta registrada correctamente.")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo registrar la monta.")
    
    def ver_montas(self):
        montas = self.master.obtener_montas()
        if not montas:
            messagebox.showinfo("Info", "No hay montas registradas.")
            return
        
        ventana = tk.Toplevel(self)
        ventana.title("Montas Registradas")
        
        columnas = ("ID", "Fecha Monta", "Cerda", "Semen", "Fecha Parto Estimado")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="center")
        
        for monta in montas:
            tree.insert("", tk.END, values=(
                monta["Id_monta"],
                monta["fecha_monta"],
                monta["cod_cerda"],
                monta["cod_semen"],
                monta["fecha_parto_estimado"]
            ))
        
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        tree.pack(expand=True, fill="both")
    
    def limpiar_formulario(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.combo_cerda.set("")
        self.combo_semen.set("")


class GestionGeneral(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")
        
        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista_con_parametros(MenuPrincipal, master.usuario_logueado, master.rol), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)
        
        label_titulo = tk.Label(barra_superior, text="GESTIÓN GENERAL", 
                                font=("Helvetica", 20, "bold"), bg="#316A99", fg="black")
        label_titulo.pack(pady=5)

        contenedor_botones = tk.Frame(self, bg="#D3D3D3")
        contenedor_botones.pack(expand=True, fill="both", pady=50)
        
        contenedor_botones.grid_rowconfigure(0, weight=1)
        for i in range(3):
            contenedor_botones.grid_columnconfigure(i, weight=1)

        estilo_boton = {
            'font': ("Helvetica", 14, "bold"),
            'bg': "#E6A9D3",
            'width': 18,  
            'height': 6,  
            'bd': 0,      
            'activebackground': "#D48FB8"  
        }

        tk.Button(
            contenedor_botones, 
            text="GESTIÓN LECHÓN", 
            command=lambda: master.mostrar_vista(Crear_Lechon),
            **estilo_boton
        ).grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        tk.Button(
            contenedor_botones, 
            text="GESTIÓN CERDAS", 
            command=lambda: master.mostrar_vista(Crear_Cerda),
            **estilo_boton
        ).grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        tk.Button(
            contenedor_botones, 
            text="GESTIÓN SEMEN", 
            command=lambda: master.mostrar_vista(Crear_Semen),
            **estilo_boton
        ).grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

class Crear_Lechon(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")
        
        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista(GestionGeneral), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)
        
        tk.Label(
            barra_superior, text="REGISTRAR LECHÓN", font=("Helvetica", 20, "bold"), 
            bg="#316A99", fg="black"
        ).pack(pady=5)
        
        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=20)
        
        campos = [
            "Código Lechón:", "Fecha Nacimiento (YYYY-MM-DD):", "Raza:", 
            "ID Madre:", "ID Lote:"
        ]
        self.entradas = {}
        
        for idx, campo in enumerate(campos):
            tk.Label(
                contenedor_formulario, text=campo, font=("Helvetica", 12), 
                bg="#D3D3D3", fg="black"
            ).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            
            entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 12))
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entrada
        
        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones, text="Crear Lechón", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.crear_lechon
        ).pack(side="left", padx=20)
        
        tk.Button(
            frame_botones, text="Ver Lechones", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.ver_lechones
        ).pack(side="left", padx=20)
    
    def crear_lechon(self):
        cod_lechon = self.entradas["Código Lechón:"].get()
        fecha_nac = self.entradas["Fecha Nacimiento (YYYY-MM-DD):"].get()
        raza = self.entradas["Raza:"].get()
        id_madre = self.entradas["ID Madre:"].get()
        id_lote = self.entradas["ID Lote:"].get()
        
        if not all([cod_lechon, fecha_nac, raza, id_madre, id_lote]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            datetime.strptime(fecha_nac, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return
        
        try:
            id_madre = int(id_madre)
            id_lote = int(id_lote)
        except ValueError:
            messagebox.showerror("Error", "ID Madre y Lote deben ser números.")
            return
        
        if self.master.insertar_lechon(cod_lechon, fecha_nac, raza, id_madre, id_lote):
            messagebox.showinfo("Éxito", "Lechón registrado correctamente.")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo registrar el lechón.")
    
    def ver_lechones(self):
        lechones = self.master.obtener_lechones()
        if not lechones:
            messagebox.showinfo("Info", "No hay lechones registrados.")
            return
        
        ventana = tk.Toplevel(self)
        ventana.title("Lechones Registrados")
        
        columnas = ("ID", "Código", "Fecha Nac.", "Raza", "ID Madre", "ID Lote")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        
        for lechon in lechones:
            tree.insert("", tk.END, values=(
                lechon["Id_lechon"],
                lechon["cod_lechon"],
                lechon["fecha_nac"],
                lechon["raza"],
                lechon["Id_madre"],
                lechon["Id_lote"]
            ))
        
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        tree.pack(expand=True, fill="both")
    
    def limpiar_formulario(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)

class Crear_Cerda(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")
        
        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista(GestionGeneral), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)
        
        tk.Label(
            barra_superior, text="REGISTRAR CERDA", font=("Helvetica", 20, "bold"), 
            bg="#316A99", fg="black"
        ).pack(pady=5)
        
        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=20)
        
        campos = [
            "Código Cerda:", "Fecha Nacimiento (YYYY-MM-DD):", "Raza:", 
            "Estado (vacia/inseminada/gestante/lactancia):"
        ]
        self.entradas = {}
        
        for idx, campo in enumerate(campos):
            tk.Label(
                contenedor_formulario, text=campo, font=("Helvetica", 12), 
                bg="#D3D3D3", fg="black"
            ).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            
            if campo == "Estado (vacia/inseminada/gestante/lactancia):":
                self.combo_estado = ttk.Combobox(
                    contenedor_formulario, 
                    values=["vacia", "inseminada", "gestante", "lactancia"],
                    font=("Helvetica", 12),
                    state="readonly"
                )
                self.combo_estado.grid(row=idx, column=1, padx=10, pady=5)
                self.combo_estado.current(0) 
            else:
                entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 12))
                entrada.grid(row=idx, column=1, padx=10, pady=5)
                self.entradas[campo] = entrada
        
        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones, text="Crear Cerda", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.crear_cerda
        ).pack(side="left", padx=20)
        
        tk.Button(
            frame_botones, text="Ver Cerdas", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.ver_cerdas
        ).pack(side="left", padx=20)
    
    def crear_cerda(self):
        cod_cerda = self.entradas["Código Cerda:"].get()
        fecha_nac = self.entradas["Fecha Nacimiento (YYYY-MM-DD):"].get()
        raza = self.entradas["Raza:"].get()
        estado = self.combo_estado.get()
        
        if not all([cod_cerda, fecha_nac, raza]):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            datetime.strptime(fecha_nac, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return
        
        if self.master.insertar_cerda(cod_cerda, fecha_nac, raza, estado):
            messagebox.showinfo("Éxito", "Cerda registrada correctamente.")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo registrar la cerda.")
    
    def ver_cerdas(self):
        cerdas = self.master.obtener_cerdas()
        if not cerdas:
            messagebox.showinfo("Info", "No hay cerdas registradas.")
            return
        
        ventana = tk.Toplevel(self)
        ventana.title("Cerdas Registradas")
        
        columnas = ("ID", "Código", "Fecha Nac.", "Raza", "Estado")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        
        for cerda in cerdas:
            tree.insert("", tk.END, values=(
                cerda["Id_cerda"],
                cerda["cod_cerda"],
                cerda["fecha_nacimiento"],
                cerda["raza"],
                cerda["estado"]
            ))
        
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        tree.pack(expand=True, fill="both")
    
    def limpiar_formulario(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self.combo_estado.current(0)

class Crear_Semen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#D3D3D3")
        
        barra_superior = tk.Frame(self, bg="#316A99", height=50)
        barra_superior.pack(fill="x")
        
        boton_volver = tk.Button(barra_superior, text="←", font=("Helvetica", 16), bg="#316A99", fg="white",
                                 command=lambda: master.mostrar_vista(GestionGeneral), borderwidth=0)
        boton_volver.pack(side="left", padx=10, pady=5)
        
        tk.Label(
            barra_superior, text="REGISTRAR SEMEN", font=("Helvetica", 20, "bold"), 
            bg="#316A99", fg="black"
        ).pack(pady=5)
        
        contenedor_formulario = tk.Frame(self, bg="#D3D3D3")
        contenedor_formulario.pack(pady=20)
        
        campos = [
            "Código Semen:", "Fecha Adquisición (YYYY-MM-DD):", 
            "Granja de Origen:", "Contacto Granja:", "Raza:"
        ]
        self.entradas = {}
        
        for idx, campo in enumerate(campos):
            tk.Label(
                contenedor_formulario, text=campo, font=("Helvetica", 12), 
                bg="#D3D3D3", fg="black"
            ).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            
            entrada = tk.Entry(contenedor_formulario, font=("Helvetica", 12))
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entrada
        
        frame_botones = tk.Frame(self, bg="#D3D3D3")
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones, text="Crear Semen", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.crear_semen
        ).pack(side="left", padx=20)
        
        tk.Button(
            frame_botones, text="Ver Semen", bg="#E6A9D3", font=("Helvetica", 14, "bold"),
            command=self.ver_semen
        ).pack(side="left", padx=20)
    
    def crear_semen(self):
        cod_semen = self.entradas["Código Semen:"].get()
        fecha_adq = self.entradas["Fecha Adquisición (YYYY-MM-DD):"].get()
        granja = self.entradas["Granja de Origen:"].get()
        contacto = self.entradas["Contacto Granja:"].get()
        raza = self.entradas["Raza:"].get()
        
        if not all([cod_semen, fecha_adq, granja, raza]):
            messagebox.showerror("Error", "Todos los campos son obligatorios excepto Contacto.")
            return
        
        try:
            datetime.strptime(fecha_adq, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return
        
        if self.master.insertar_semen(cod_semen, fecha_adq, granja, contacto, raza):
            messagebox.showinfo("Éxito", "Semen registrado correctamente.")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", "No se pudo registrar el semen.")
    
    def ver_semen(self):
        semen = self.master.obtener_semen()
        if not semen:
            messagebox.showinfo("Info", "No hay semen registrado.")
            return
        
        ventana = tk.Toplevel(self)
        ventana.title("Semen Registrado")
        
        columnas = ("ID", "Código", "Fecha Adq.", "Granja", "Contacto", "Raza")
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        
        for item in semen:
            tree.insert("", tk.END, values=(
                item["Id_semen"],
                item["cod_semen"],
                item["fecha_adquisicion"],
                item["granja_adquisicion"],
                item["contacto_granja"],
                item["raza"]
            ))
        
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        tree.pack(expand=True, fill="both")
    
    def limpiar_formulario(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
