# Importación de la biblioteca tkinter para construir interfaces gráficas (GUI)
import tkinter as tk
# Importación de ttk, una extensión de tkinter que ofrece widgets con un diseño más moderno
from tkinter import ttk
# messagebox permite crear cuadros de diálogo para mostrar mensajes al usuario
from tkinter import messagebox
# Importación de mysql.connector para conectar y realizar operaciones en una base de datos MySQL
import mysql.connector
# matplotlib.pyplot es una biblioteca para generar gráficos en 2D
import matplotlib.pyplot as plt
# pandas es una biblioteca utilizada para la manipulación y análisis de datos estructurados
import pandas as pd
# tkinter.filedialog proporciona herramientas para interactuar con el sistema de archivos (como abrir o guardar archivos)
import tkinter.filedialog as fd
# seaborn es una biblioteca para visualización de datos basada en matplotlib, especializada en gráficos estadísticos
import seaborn as sns


# Definición de la función para conectar a la base de datos
def connect_to_db():
    # Retorna una conexión a la base de datos MySQL utilizando mysql.connector.connect()
    return mysql.connector.connect(
        host="localhost",       # Dirección del servidor de la base de datos (en este caso, el servidor local)
        user="root",            # Nombre de usuario para acceder a la base de datos
        password="campusfp",    # Contraseña para el usuario de la base de datos
        database="ENCUESTAS"    # Nombre de la base de datos a la que se desea conectar
    )


# Definición de la función para validar entradas de números enteros
def validate_int_input(value):
    # Retorna True si el valor es un número entero (solo dígitos) o si el valor es una cadena vacía
    return value.isdigit() or value == ""


# Definición de la función para agregar una encuesta a la base de datos
def add_encuesta():
    try:
        # Obtener y limpiar la entrada de edad del campo de texto
        edad = entry_age.get().strip()
        
        # Validar que la edad sea un número válido
        if not edad.isdigit():
            messagebox.showwarning("Advertencia", "La edad debe ser un número válido.")
            return  # Detener la ejecución si la edad no es válida

        # Obtener y limpiar las entradas de los demás campos de texto
        bebidas_semana = entry_beverages_week.get().strip()
        cervezas_semana = entry_beers_week.get().strip()
        bebidas_fin_semana = entry_beverages_weekend.get().strip()
        bebidas_destiladas_semana = entry_distilled_week.get().strip()
        vino_semana = entry_wine_week.get().strip()
        perdida_control = entry_control_loss.get().strip()
        dependencia = entry_dependence.get().strip()
        problemas_digestivos = entry_digestive_issues.get().strip()
        tension_alta = entry_high_tension.get().strip()
        dolor_cabeza = entry_headache.get().strip()

        # Validar que los campos de consumo sean números válidos
        if not (bebidas_semana.isdigit() and cervezas_semana.isdigit() and
                bebidas_fin_semana.isdigit() and bebidas_destiladas_semana.isdigit() and
                vino_semana.isdigit()):
            messagebox.showwarning("Advertencia", "Los campos de consumo deben ser números válidos.")
            return  # Detener la ejecución si algún campo no es válido

        # Establecer conexión con la base de datos
        conn = connect_to_db()
        cursor = conn.cursor()

        # SQL para insertar una nueva encuesta en la tabla ENCUESTA
        sql = ("INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, "
               "BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, "
               "ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        # Ejecutar la consulta SQL con los valores obtenidos del formulario
        cursor.execute(sql, (
            int(edad),                    # Edad convertida a entero
            entry_gender.get(),           # Sexo seleccionado en el formulario
            int(bebidas_semana),          # Consumo semanal de bebidas convertido a entero
            int(cervezas_semana),         # Consumo semanal de cervezas convertido a entero
            int(bebidas_fin_semana),      # Consumo de bebidas en fin de semana convertido a entero
            int(bebidas_destiladas_semana), # Consumo semanal de bebidas destiladas convertido a entero
            int(vino_semana),             # Consumo semanal de vino convertido a entero
            int(perdida_control),         # Indicador de pérdida de control (entero)
            dependencia,                  # Dependencia alcohólica (texto o valor binario)
            problemas_digestivos,         # Problemas digestivos relacionados (texto o valor binario)
            tension_alta,                 # Problemas de tensión alta (texto o valor binario)
            dolor_cabeza                  # Dolor de cabeza asociado (texto o valor binario)
        ))

        # Confirmar los cambios en la base de datos
        conn.commit()
        
        # Mostrar un mensaje informativo al usuario
        messagebox.showinfo("Info", "Encuesta agregada correctamente")

        # Limpiar los campos de entrada después de insertar la encuesta
        clear_entries()

        # Actualizar la tabla o lista que muestra los datos
        show_data()

    except Exception as e:
        # Mostrar un mensaje de error si algo falla
        messagebox.showerror("Error", f"Error al agregar la encuesta: {e}")
    finally:
        # Asegurarse de cerrar la conexión con la base de datos
        conn.close()


# Definición de la función para limpiar todos los campos de entrada en el formulario
def clear_entries():
    # Borra el contenido del campo de entrada de la edad
    entry_age.delete(0, tk.END)
    # Borra el contenido del campo de entrada del género
    entry_gender.delete(0, tk.END)
    # Borra el contenido del campo de entrada del consumo semanal de bebidas
    entry_beverages_week.delete(0, tk.END)
    # Borra el contenido del campo de entrada del consumo semanal de cervezas
    entry_beers_week.delete(0, tk.END)
    # Borra el contenido del campo de entrada del consumo de bebidas en el fin de semana
    entry_beverages_weekend.delete(0, tk.END)
    # Borra el contenido del campo de entrada del consumo semanal de bebidas destiladas
    entry_distilled_week.delete(0, tk.END)
    # Borra el contenido del campo de entrada del consumo semanal de vino
    entry_wine_week.delete(0, tk.END)
    # Borra el contenido del campo de entrada de la pérdida de control
    entry_control_loss.delete(0, tk.END)
    # Borra el contenido del campo de entrada de la dependencia al alcohol
    entry_dependence.delete(0, tk.END)
    # Borra el contenido del campo de entrada de los problemas digestivos
    entry_digestive_issues.delete(0, tk.END)
    # Borra el contenido del campo de entrada de la tensión alta
    entry_high_tension.delete(0, tk.END)
    # Borra el contenido del campo de entrada del dolor de cabeza
    entry_headache.delete(0, tk.END)


# Definición de la función para mostrar los datos almacenados en la base de datos
def show_data():
    try:
        # Establece una conexión con la base de datos utilizando la función connect_to_db()
        conn = connect_to_db()
        cursor = conn.cursor()

        # Ejecuta una consulta SQL para obtener todos los registros de la tabla ENCUESTA
        cursor.execute("SELECT * FROM ENCUESTA")

        # Recupera todos los resultados de la consulta como una lista de filas
        rows = cursor.fetchall()

        # Elimina cualquier dato existente en el widget "tree" antes de insertar nuevos datos
        for row in tree.get_children():
            tree.delete(row)

        # Inserta cada fila recuperada de la base de datos en el widget "tree"
        for row in rows:
            tree.insert("", "end", values=row)

    except Exception as e:
        # Si ocurre un error, muestra un cuadro de diálogo con el mensaje del error
        messagebox.showerror("Error", f"No se pudo recuperar la información: {e}")

    finally:
        # Asegura que la conexión con la base de datos se cierre, incluso si ocurre un error
        conn.close()


# Definición de la función para eliminar una encuesta seleccionada
def delete_encuesta():
    # Obtiene los elementos seleccionados en el widget "tree"
    selected_item = tree.selection()

    # Verifica si no se seleccionó ningún elemento
    if not selected_item:

        # Muestra una advertencia si no hay elementos seleccionados
        messagebox.showwarning("Warning", "Selecciona un registro para eliminar")
        return  # Termina la ejecución si no hay selección

    try:
        # Conectar a la base de datos
        conn = connect_to_db()
        cursor = conn.cursor()
        # Recorre los elementos seleccionados
        for item in selected_item:
            # Obtiene el ID de la encuesta desde el primer valor de la fila seleccionada
            idEncuesta = tree.item(item, 'values')[0]

            # Ejecuta un comando SQL para eliminar el registro correspondiente en la base de datos
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (idEncuesta,))

            # Elimina el elemento también del widget "tree"
            tree.delete(item)

        # Confirma los cambios en la base de datos
        conn.commit()
        # Muestra un mensaje informativo de éxito
        messagebox.showinfo("Info", "Encuesta eliminada correctamente")

    except Exception as e:
        # Si ocurre un error, muestra un mensaje de error al usuario
        messagebox.showerror("Error", f"Error al eliminar la encuesta: {e}")

    finally:
        # Cierra la conexión con la base de datos
        conn.close()


# Definición de la función para cargar una encuesta seleccionada en los campos del formulario
def load_encuesta():
    # Obtiene el elemento seleccionado en el widget "tree"
    selected_item = tree.selection()

    # Verifica si no hay ningún elemento seleccionado
    if not selected_item:
        # Muestra una advertencia si no hay selección
        messagebox.showwarning("Warning", "Selecciona un registro para cargar")
        return  # Termina la ejecución si no hay selección

    # Obtiene los valores de la fila seleccionada
    item = tree.item(selected_item[0])
    values = item['values']

    # Limpia y carga los valores correspondientes en cada campo del formulario
    entry_age.delete(0, tk.END)
    entry_age.insert(0, values[1])  # Edad

    entry_gender.delete(0, tk.END)
    entry_gender.insert(0, values[2])  # Género

    entry_beverages_week.delete(0, tk.END)
    entry_beverages_week.insert(0, values[3])  # Bebidas semana

    entry_beers_week.delete(0, tk.END)
    entry_beers_week.insert(0, values[4])  # Cervezas semana

    entry_beverages_weekend.delete(0, tk.END)
    entry_beverages_weekend.insert(0, values[5])  # Bebidas fin de semana

    entry_distilled_week.delete(0, tk.END)
    entry_distilled_week.insert(0, values[6])  # Bebidas destiladas semana

    entry_wine_week.delete(0, tk.END)
    entry_wine_week.insert(0, values[7])  # Vino semana

    entry_control_loss.delete(0, tk.END)
    entry_control_loss.insert(0, values[8])  # Pérdida de control

    entry_dependence.delete(0, tk.END)
    entry_dependence.insert(0, values[9])  # Dependencia al alcohol

    entry_digestive_issues.delete(0, tk.END)
    entry_digestive_issues.insert(0, values[10])  # Problemas digestivos

    entry_high_tension.delete(0, tk.END)
    entry_high_tension.insert(0, values[11])  # Tensión alta

    entry_headache.delete(0, tk.END)
    entry_headache.insert(0, values[12])  # Dolor de cabeza


# Definición de la función para actualizar un registro seleccionado en la base de datos
def update_encuesta():
    # Obtiene el elemento seleccionado en el widget "tree"
    selected_item = tree.selection()

    # Verifica si no hay ningún elemento seleccionado
    if not selected_item:
        # Muestra una advertencia si no hay selección
        messagebox.showwarning("Warning", "Selecciona un registro para actualizar")
        return  # Termina la ejecución si no hay selección

    try:
        # Obtiene el ID del registro seleccionado desde el primer valor (columna) del elemento seleccionado
        idEncuesta = tree.item(selected_item[0], 'values')[0]

        # Conecta a la base de datos
        conn = connect_to_db()
        cursor = conn.cursor()

        # Consulta SQL para actualizar los datos del registro seleccionado
        sql = (
            "UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, "
            "BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, "
            "ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s"
        )

        # Ejecuta la consulta de actualización con los valores obtenidos de los campos del formulario
        cursor.execute(sql, (
            int(entry_age.get()),           # Edad
            entry_gender.get(),             # Género
            int(entry_beverages_week.get()),# Bebidas por semana
            int(entry_beers_week.get()),    # Cervezas por semana
            int(entry_beverages_weekend.get()), # Bebidas en fin de semana
            int(entry_distilled_week.get()),    # Bebidas destiladas por semana
            int(entry_wine_week.get()),         # Vinos por semana
            int(entry_control_loss.get()),      # Pérdida de control
            entry_dependence.get(),             # Dependencia al alcohol
            entry_digestive_issues.get(),       # Problemas digestivos
            entry_high_tension.get(),           # Tensión alta
            entry_headache.get(),               # Dolor de cabeza
            idEncuesta                           # ID del registro a actualizar
        ))

        # Confirma los cambios en la base de datos
        conn.commit()

        # Muestra un mensaje informativo de éxito
        messagebox.showinfo("Info", "Encuesta actualizada correctamente")

        # Actualiza los datos en el widget "tree" mostrando los cambios
        show_data()

        # Limpia los campos del formulario
        clear_entries()

    except Exception as e:
        # Si ocurre un error, muestra un mensaje de error al usuario
        messagebox.showerror("Error", f"Error al actualizar la encuesta: {e}")

    finally:
        # Cierra la conexión con la base de datos
        conn.close()


# Crea la ventana principal de la aplicación
root = tk.Tk()

# Define el título de la ventana
root.title("Sistema de Encuestas de Salud")

# Define el tamaño de la ventana
root.geometry("900x800")

# Cambia el color de fondo de la ventana
root.config(bg="#f2f2f2")

# Registro para validar que solo se introduzcan números enteros en los campos
vcmd = (root.register(validate_int_input), '%P')

# Crea un marco para los campos del formulario
form_frame = tk.Frame(root, bg="#e6e6e6", padx=10, pady=10)

# Empaqueta el marco para que ocupe todo el ancho de la ventana
form_frame.pack(fill="x", padx=10, pady=10)

# Crea la etiqueta y campo de entrada para la edad
tk.Label(form_frame, text="Edad:", bg="#e6e6e6").grid(row=0, column=0, sticky="w")
entry_age = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_age.grid(row=0, column=1)

# Crea la etiqueta y campo de entrada para el sexo
tk.Label(form_frame, text="Sexo:", bg="#e6e6e6").grid(row=0, column=2, sticky="w")
entry_gender = tk.Entry(form_frame)
entry_gender.grid(row=0, column=3)

# Crea la etiqueta y campo de entrada para bebidas consumidas durante la semana
tk.Label(form_frame, text="Bebidas Semana:", bg="#e6e6e6").grid(row=1, column=0, sticky="w")
entry_beverages_week = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beverages_week.grid(row=1, column=1)

# Crea la etiqueta y campo de entrada para cervezas consumidas durante la semana
tk.Label(form_frame, text="Cervezas Semana:", bg="#e6e6e6").grid(row=1, column=2, sticky="w")
entry_beers_week = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beers_week.grid(row=1, column=3)

# Crea la etiqueta y campo de entrada para bebidas consumidas durante el fin de semana
tk.Label(form_frame, text="Bebidas Fin de Semana:", bg="#e6e6e6").grid(row=2, column=0, sticky="w")
entry_beverages_weekend = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beverages_weekend.grid(row=2, column=1)

# Crea la etiqueta y campo de entrada para bebidas destiladas consumidas durante la semana
tk.Label(form_frame, text="Bebidas Destiladas Semana:", bg="#e6e6e6").grid(row=2, column=2, sticky="w")
entry_distilled_week = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_distilled_week.grid(row=2, column=3)

# Crea la etiqueta y campo de entrada para vino consumido durante la semana
tk.Label(form_frame, text="Vino Semana:", bg="#e6e6e6").grid(row=3, column=0, sticky="w")
entry_wine_week = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_wine_week.grid(row=3, column=1)

# Crea la etiqueta y campo de entrada para pérdida de control relacionada con el consumo
tk.Label(form_frame, text="Perdida de Control:", bg="#e6e6e6").grid(row=3, column=2, sticky="w")
entry_control_loss = tk.Entry(form_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_control_loss.grid(row=3, column=3)

# Crea la etiqueta y campo de entrada para dependencia o diversión relacionada con el consumo
tk.Label(form_frame, text="Dependencia Diversión:", bg="#e6e6e6").grid(row=4, column=0, sticky="w")
entry_dependence = tk.Entry(form_frame)
entry_dependence.grid(row=4, column=1)

# Crea la etiqueta y campo de entrada para problemas digestivos relacionados con el consumo
tk.Label(form_frame, text="Problemas Digestivos:", bg="#e6e6e6").grid(row=4, column=2, sticky="w")
entry_digestive_issues = tk.Entry(form_frame)
entry_digestive_issues.grid(row=4, column=3)

# Crea la etiqueta y campo de entrada para tensión alta relacionada con el consumo
tk.Label(form_frame, text="Tensión Alta:", bg="#e6e6e6").grid(row=5, column=0, sticky="w")
entry_high_tension = tk.Entry(form_frame)
entry_high_tension.grid(row=5, column=1)

# Crea la etiqueta y campo de entrada para dolor de cabeza relacionado con el consumo
tk.Label(form_frame, text="Dolor de Cabeza:", bg="#e6e6e6").grid(row=5, column=2, sticky="w")
entry_headache = tk.Entry(form_frame)
entry_headache.grid(row=5, column=3)

# Crea un marco para los botones de acción
button_frame = tk.Frame(root, bg="#f2f2f2")

# Empaqueta el marco de botones
button_frame.pack(fill="x", padx=10, pady=10)

# Crea los botones de la interfaz para agregar, eliminar, actualizar, cargar y mostrar datos
tk.Button(button_frame, text="Agregar Encuesta", command=add_encuesta, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Eliminar Encuesta", command=delete_encuesta, bg="#f44336", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Actualizar Encuesta", command=update_encuesta, bg="#FFC107", fg="white").grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Cargar Encuesta", command=load_encuesta, bg="#00BCD4", fg="white").grid(row=0, column=3, padx=5, pady=5)
tk.Button(button_frame, text="Mostrar Datos", command=show_data, bg="#607D8B", fg="white").grid(row=0, column=4, padx=5, pady=5)


# Crea un marco para el filtro de encuestas
filter_frame = tk.Frame(root, bg="#d9d9d9", padx=10, pady=10)

# Empaqueta el marco para que ocupe todo el ancho de la ventana
filter_frame.pack(fill="x", padx=10, pady=10)

# Crea la etiqueta y campo de entrada para la edad mínima
tk.Label(filter_frame, text="Edad Min:", bg="#d9d9d9").grid(row=0, column=0, sticky="w")
entry_age_min = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_age_min.grid(row=0, column=1)

# Crea la etiqueta y campo de entrada para la edad máxima
tk.Label(filter_frame, text="Edad Max:", bg="#d9d9d9").grid(row=0, column=2, sticky="w")
entry_age_max = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_age_max.grid(row=0, column=3)

# Crea la etiqueta y campo de entrada para el sexo
tk.Label(filter_frame, text="Sexo:", bg="#d9d9d9").grid(row=0, column=4, sticky="w")
entry_gender_filter = tk.Entry(filter_frame)
entry_gender_filter.grid(row=0, column=5)

# Crea la etiqueta y campo de entrada para el consumo mínimo de bebidas durante la semana
tk.Label(filter_frame, text="Consumo Bebidas Semana Min:", bg="#d9d9d9").grid(row=1, column=0, sticky="w")
entry_beverages_week_min = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beverages_week_min.grid(row=1, column=1)

# Crea la etiqueta y campo de entrada para el consumo máximo de bebidas durante la semana
tk.Label(filter_frame, text="Consumo Bebidas Semana Max:", bg="#d9d9d9").grid(row=1, column=2, sticky="w")
entry_beverages_week_max = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beverages_week_max.grid(row=1, column=3)

# Crea la etiqueta y campo de entrada para el consumo mínimo de cervezas durante la semana
tk.Label(filter_frame, text="Consumo Cervezas Min:", bg="#d9d9d9").grid(row=2, column=0, sticky="w")
entry_beers_week_min = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beers_week_min.grid(row=2, column=1)

# Crea la etiqueta y campo de entrada para el consumo máximo de cervezas durante la semana
tk.Label(filter_frame, text="Consumo Cervezas Max:", bg="#d9d9d9").grid(row=2, column=2, sticky="w")
entry_beers_week_max = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beers_week_max.grid(row=2, column=3)

# Crea la etiqueta y campo de entrada para problemas digestivos
tk.Label(filter_frame, text="Problemas Digestivos:", bg="#d9d9d9").grid(row=3, column=0, sticky="w")
entry_digestive_issues_filter = tk.Entry(filter_frame)
entry_digestive_issues_filter.grid(row=3, column=1)

# Crea la etiqueta y campo de entrada para tensión alta
tk.Label(filter_frame, text="Tensión Alta:", bg="#d9d9d9").grid(row=3, column=2, sticky="w")
entry_high_tension_filter = tk.Entry(filter_frame)
entry_high_tension_filter.grid(row=3, column=3)

# Crea la etiqueta y campo de entrada para el consumo mínimo de vino durante la semana
tk.Label(filter_frame, text="Vino Semana Min:", bg="#d9d9d9").grid(row=4, column=0, sticky="w")
entry_wine_week_min = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_wine_week_min.grid(row=4, column=1)

# Crea la etiqueta y campo de entrada para el consumo máximo de vino durante la semana
tk.Label(filter_frame, text="Vino Semana Max:", bg="#d9d9d9").grid(row=4, column=2, sticky="w")
entry_wine_week_max = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_wine_week_max.grid(row=4, column=3)

# Crea la etiqueta y campo de entrada para el consumo mínimo de bebidas durante el fin de semana
tk.Label(filter_frame, text="Bebidas Fin de Semana Min:", bg="#d9d9d9").grid(row=5, column=0, sticky="w")
entry_beverages_weekend_min = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beverages_weekend_min.grid(row=5, column=1)

# Crea la etiqueta y campo de entrada para el consumo máximo de bebidas durante el fin de semana
tk.Label(filter_frame, text="Bebidas Fin de Semana Max:", bg="#d9d9d9").grid(row=5, column=2, sticky="w")
entry_beverages_weekend_max = tk.Entry(filter_frame, validate="key", validatecommand=vcmd)  # Validación para solo números
entry_beverages_weekend_max.grid(row=5, column=3)


# Función para filtrar los datos de la base de datos según los criterios ingresados
def filter_data():
    try:
        # Conectarse a la base de datos
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Comienza la consulta SQL con una condición siempre verdadera (1=1) 
        # para poder ir agregando filtros sin complicaciones
        sql = "SELECT * FROM ENCUESTA WHERE 1=1"
        params = []  # Lista para almacenar los parámetros de los filtros
        
        # Filtro de edad mínima: Si el campo de edad mínima tiene valor, se agrega el filtro correspondiente
        if entry_age_min.get():
            sql += " AND edad >= %s"  # Se agrega una condición para la edad mínima
            params.append(int(entry_age_min.get()))  # Se agrega el valor de la edad mínima a los parámetros
        
        # Filtro de edad máxima: Si el campo de edad máxima tiene valor, se agrega el filtro correspondiente
        if entry_age_max.get():
            sql += " AND edad <= %s"  # Se agrega una condición para la edad máxima
            params.append(int(entry_age_max.get()))  # Se agrega el valor de la edad máxima a los parámetros
        
        # Filtro de sexo: Si el campo de sexo tiene valor, se agrega el filtro correspondiente
        if entry_gender_filter.get():
            sql += " AND Sexo = %s"  # Se agrega una condición para el sexo
            params.append(entry_gender_filter.get())  # Se agrega el valor del sexo a los parámetros
        
        # Filtro de consumo de bebidas durante la semana (mínimo): Si el campo tiene valor, se agrega el filtro
        if entry_beverages_week_min.get():
            sql += " AND BebidasSemana >= %s"  # Se agrega una condición para el consumo mínimo de bebidas
            params.append(int(entry_beverages_week_min.get()))  # Se agrega el valor del consumo mínimo a los parámetros
        
        # Filtro de consumo de bebidas durante la semana (máximo): Si el campo tiene valor, se agrega el filtro
        if entry_beverages_week_max.get():
            sql += " AND BebidasSemana <= %s"  # Se agrega una condición para el consumo máximo de bebidas
            params.append(int(entry_beverages_week_max.get()))  # Se agrega el valor del consumo máximo a los parámetros
        
        # Filtro de consumo de cervezas durante la semana (mínimo): Si el campo tiene valor, se agrega el filtro
        if entry_beers_week_min.get():
            sql += " AND CervezasSemana >= %s"  # Se agrega una condición para el consumo mínimo de cervezas
            params.append(int(entry_beers_week_min.get()))  # Se agrega el valor del consumo mínimo a los parámetros
        
        # Filtro de consumo de cervezas durante la semana (máximo): Si el campo tiene valor, se agrega el filtro
        if entry_beers_week_max.get():
            sql += " AND CervezasSemana <= %s"  # Se agrega una condición para el consumo máximo de cervezas
            params.append(int(entry_beers_week_max.get()))  # Se agrega el valor del consumo máximo a los parámetros
        
        # Filtro de problemas digestivos: Si el campo tiene valor, se agrega el filtro correspondiente
        if entry_digestive_issues_filter.get():
            sql += " AND ProblemasDigestivos = %s"  # Se agrega una condición para problemas digestivos
            params.append(entry_digestive_issues_filter.get())  # Se agrega el valor de problemas digestivos a los parámetros
        
        # Filtro de tensión alta: Si el campo tiene valor, se agrega el filtro correspondiente
        if entry_high_tension_filter.get():
            sql += " AND TensionAlta = %s"  # Se agrega una condición para tensión alta
            params.append(entry_high_tension_filter.get())  # Se agrega el valor de tensión alta a los parámetros
        
        # Filtro de consumo de vino durante la semana (mínimo): Si el campo tiene valor, se agrega el filtro
        if entry_wine_week_min.get():
            sql += " AND VinosSemana >= %s"  # Se agrega una condición para el consumo mínimo de vino
            params.append(int(entry_wine_week_min.get()))  # Se agrega el valor del consumo mínimo de vino a los parámetros
        
        # Filtro de consumo de vino durante la semana (máximo): Si el campo tiene valor, se agrega el filtro
        if entry_wine_week_max.get():
            sql += " AND VinosSemana <= %s"  # Se agrega una condición para el consumo máximo de vino
            params.append(int(entry_wine_week_max.get()))  # Se agrega el valor del consumo máximo de vino a los parámetros
        
        # Filtro de consumo de bebidas durante el fin de semana (mínimo): Si el campo tiene valor, se agrega el filtro
        if entry_beverages_weekend_min.get():
            sql += " AND BebidasFinSemana >= %s"  # Se agrega una condición para el consumo mínimo de bebidas en fin de semana
            params.append(int(entry_beverages_weekend_min.get()))  # Se agrega el valor del consumo mínimo a los parámetros
        
        # Filtro de consumo de bebidas durante el fin de semana (máximo): Si el campo tiene valor, se agrega el filtro
        if entry_beverages_weekend_max.get():
            sql += " AND BebidasFinSemana <= %s"  # Se agrega una condición para el consumo máximo de bebidas en fin de semana
            params.append(int(entry_beverages_weekend_max.get()))  # Se agrega el valor del consumo máximo a los parámetros

        # Ejecuta la consulta SQL con los parámetros correspondientes
        cursor.execute(sql, params)
        rows = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        
        # Borra los datos actuales en el árbol (tabla) antes de insertar los nuevos resultados filtrados
        for row in tree.get_children():
            tree.delete(row)
        
        # Inserta los resultados filtrados en el árbol (tabla)
        for row in rows:
            tree.insert("", "end", values=row)  # Inserta cada fila en el árbol

    except Exception as e:
        # Si ocurre un error, muestra un mensaje de error
        messagebox.showerror("Error", f"Error al aplicar filtros: {e}")
    
    finally:
        # Cierra la conexión a la base de datos
        conn.close()

# Botón para aplicar los filtros y mostrar los resultados filtrados en la tabla
tk.Button(filter_frame, text="Mostrar Datos Filtrados", command=filter_data, bg="#607D8B", fg="white").grid(row=6, column=0, columnspan=6, pady=5)


def export_to_excel():
    try:
        # Recuperar los datos visibles en el Treeview.
        # Esto obtiene las filas de datos del Treeview donde cada fila corresponde a un ítem en el Treeview.
        rows = [tree.item(item, 'values') for item in tree.get_children()]

        # Si no hay filas (datos) en el Treeview, muestra un mensaje de advertencia.
        if not rows:
            messagebox.showwarning("Advertencia", "No hay datos para exportar.")
            return  # Sale de la función si no hay datos para exportar.

        # Definir los nombres de las columnas que se utilizarán en el DataFrame.
        columns = ("idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", 
                   "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", 
                   "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", 
                   "TensionAlta", "DolorCabeza")
        
        # Crear un DataFrame a partir de las filas obtenidas del Treeview y las columnas definidas.
        df = pd.DataFrame(rows, columns=columns)

        # Solicitar al usuario que seleccione la ubicación y el nombre del archivo donde se guardará el Excel.
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                                   filetypes=[("Archivos Excel", "*.xlsx")])

        # Si el usuario selecciona un archivo, proceder a exportar los datos a ese archivo Excel.
        if file_path:
            # Exportar el DataFrame a un archivo Excel sin incluir los índices del DataFrame.
            df.to_excel(file_path, index=False, engine='openpyxl')
            
            # Mostrar un mensaje informando que los datos fueron exportados correctamente.
            messagebox.showinfo("Info", "Datos exportados correctamente a Excel.")
        else:
            # Si no se seleccionó un archivo, muestra un mensaje de advertencia.
            messagebox.showwarning("Advertencia", "No se seleccionó un archivo para guardar.")

    except Exception as e:
        # Si ocurre algún error durante el proceso, mostrar un mensaje de error con el detalle.
        messagebox.showerror("Error", f"Error al exportar los datos a Excel: {e}")


# Crear un botón en la interfaz gráfica que ejecute la función `export_to_excel` cuando se haga clic.
tk.Button(button_frame, text="Exportar a Excel", command=export_to_excel, bg="#4CAF50", fg="white").grid(row=0, column=5, padx=5, pady=5)


def generate_graph():
    try:
        # Conectar a la base de datos
        # Establecemos la conexión a la base de datos utilizando la función `connect_to_db()`.
        conn = connect_to_db()
        cursor = conn.cursor()

        # Ejecutar una consulta SQL para obtener los datos necesarios
        cursor.execute("SELECT Edad, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana FROM ENCUESTA")
        rows = cursor.fetchall()  # Recuperar todas las filas de la consulta.

        # Si no se obtienen datos, mostrar un mensaje de advertencia y salir de la función.
        if not rows:
            messagebox.showwarning("Advertencia", "No hay datos para graficar.")
            return

        # Convertir los datos obtenidos en un DataFrame de pandas
        # Los datos obtenidos se almacenan en un DataFrame, que es una estructura tabular muy útil en pandas.
        df = pd.DataFrame(rows, columns=["Edad", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana"])

        # Filtrar los datos para eliminar filas con valores nulos o con cero en alguna de las columnas de bebidas.
        df = df[(df[['BebidasSemana', 'CervezasSemana', 'BebidasFinSemana', 'BebidasDestiladasSemana', 'VinosSemana']].gt(0).any(axis=1))]

        # Si el DataFrame está vacío después de filtrar, mostrar una advertencia y salir de la función.
        if df.empty:
            messagebox.showwarning("Advertencia", "No hay datos relevantes para graficar.")
            return

        # Crear grupos de edades
        # Definimos los rangos de edades y las etiquetas que los representarán.
        bins = [18, 25, 35, 45, 55, 65, 100]  # Los límites de cada grupo de edad.
        labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']  # Las etiquetas para los grupos de edad.
        
        # Asignar a cada fila un grupo de edad correspondiente basado en la columna 'Edad'.
        df['GrupoEdad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

        # Agrupar los datos por 'GrupoEdad' y calcular la suma del consumo de cada tipo de bebida en cada grupo.
        grouped = df.groupby('GrupoEdad').agg({
            'BebidasSemana': 'sum',
            'CervezasSemana': 'sum',
            'BebidasFinSemana': 'sum',
            'BebidasDestiladasSemana': 'sum',
            'VinosSemana': 'sum'
        }).sum(axis=1)  # Sumar todos los consumos de bebidas para cada grupo de edad.

        # Crear un gráfico circular (Pie Chart) con los datos agrupados por grupo de edad
        fig, ax = plt.subplots(figsize=(8, 8))  # Crear una figura y un eje para el gráfico.
        ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2", len(grouped)))
        ax.set_title('Distribución de Consumo de Bebidas por Grupo de Edad', fontsize=16, weight='bold')  # Título del gráfico.

        # Mostrar el gráfico circular.
        plt.axis('equal')  # Garantizar que el gráfico sea un círculo perfecto (no una elipse).
        plt.show()  # Mostrar el gráfico.

    except Exception as e:
        # Si ocurre algún error, mostrar un mensaje de error con detalles sobre el problema.
        messagebox.showerror("Error", f"Error al generar el gráfico: {e}")
    
    finally:
        # Cerrar la conexión a la base de datos para liberar recursos.
        conn.close()


def generate_graph_barras():
    try:
        # Conectar a la base de datos
        # Establece la conexión con la base de datos utilizando la función `connect_to_db()`.
        conn = connect_to_db()
        cursor = conn.cursor()

        # Ejecutar una consulta SQL para obtener los datos de la encuesta
        cursor.execute("SELECT Edad, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana FROM ENCUESTA")
        rows = cursor.fetchall()  # Recuperar todas las filas de los resultados de la consulta.

        # Si no hay datos, mostrar un mensaje de advertencia y salir de la función.
        if not rows:
            messagebox.showwarning("Advertencia", "No hay datos para graficar.")
            return

        # Convertir los datos en un DataFrame de pandas
        # Los datos obtenidos de la base de datos se convierten en un DataFrame, lo que facilita la manipulación de los datos.
        df = pd.DataFrame(rows, columns=["Edad", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana"])

        # Filtrar los datos para eliminar filas con valores nulos o cero en las columnas de bebidas.
        df = df[(df[['BebidasSemana', 'CervezasSemana', 'BebidasFinSemana', 'BebidasDestiladasSemana', 'VinosSemana']].gt(0).any(axis=1))]

        # Si el DataFrame está vacío después de filtrar los datos, mostrar una advertencia y salir de la función.
        if df.empty:
            messagebox.showwarning("Advertencia", "No hay datos relevantes para graficar.")
            return

        # Crear grupos de edades
        # Definir los rangos de edad y las etiquetas correspondientes.
        bins = [18, 25, 35, 45, 55, 65, 100]  # Limites de los grupos de edad.
        labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']  # Etiquetas para cada grupo de edad.
        
        # Asignar a cada fila un grupo de edad correspondiente en la nueva columna 'GrupoEdad'.
        df['GrupoEdad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

        # Agrupar los datos por 'GrupoEdad' y sumar el consumo de bebidas en cada grupo.
        # `agg()` calcula la suma de las bebidas por cada grupo de edad y luego se suman todas las bebidas para cada grupo.
        grouped = df.groupby('GrupoEdad').agg({
            'BebidasSemana': 'sum',
            'CervezasSemana': 'sum',
            'BebidasFinSemana': 'sum',
            'BebidasDestiladasSemana': 'sum',
            'VinosSemana': 'sum'
        }).sum(axis=1)  # Sumar los consumos de bebidas por grupo de edad.

        # Crear un gráfico de barras con la distribución del consumo de bebidas por grupo de edad.
        fig, ax = plt.subplots(figsize=(10, 6))  # Crear una figura con un tamaño personalizado (10x6 pulgadas).
        
        # Graficar los datos usando un gráfico de barras.
        # `kind='bar'` especifica que se quiere un gráfico de barras.
        grouped.plot(kind='bar', ax=ax, color=sns.color_palette("Set2", len(grouped)))
        
        # Configurar el título del gráfico.
        ax.set_title('Distribución de Consumo de Bebidas por Grupo de Edad', fontsize=16, weight='bold')
        
        # Configurar las etiquetas de los ejes X y Y.
        ax.set_xlabel('Grupo de Edad', fontsize=12)
        ax.set_ylabel('Consumo Total de Bebidas', fontsize=12)
        
        # Rotar las etiquetas del eje X para que se lean mejor.
        plt.xticks(rotation=45)

        # Mostrar el gráfico.
        plt.show()

    except Exception as e:
        # Si ocurre un error en cualquier parte del proceso, mostrar un mensaje de error con los detalles.
        messagebox.showerror("Error", f"Error al generar el gráfico: {e}")
    
    finally:
        # Cerrar la conexión a la base de datos para liberar recursos.
        conn.close()


# Crear un botón para generar el gráfico circular
# Este botón ejecuta la función `generate_graph()` cuando se hace clic.
# Se coloca en el `button_frame`, con texto "Generar Gráfico Circular" y un color de fondo violeta.
tk.Button(button_frame, text="Generar Gráfico Circular", command=generate_graph, bg="#8E44AD", fg="white").grid(row=0, column=6, padx=5, pady=5)

# Crear un botón para generar el gráfico de barras
# Este botón ejecuta la función `generate_graph_barras()` cuando se hace clic.
# Se coloca en el `button_frame`, con texto "Generar Gráfico Barras" y un color de fondo marrón.
tk.Button(button_frame, text="Generar Gráfico Barras", command=generate_graph_barras, bg="#804000", fg="white").grid(row=0, column=7, padx=5, pady=5)

# Definir las columnas que se mostrarán en el Treeview
# Estas columnas corresponden a los datos que se mostrarán en la tabla.
columns = (
    "idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", 
    "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", 
    "ProblemasDigestivos", "TensionAlta", "DolorCabeza"
)

# Crear un Treeview para mostrar los datos
# El Treeview es un widget que permite mostrar datos tabulares. En este caso, se configura para mostrar las columnas definidas.
tree = ttk.Treeview(root, columns=columns, show="headings")

# Configurar los encabezados de cada columna en el Treeview
# Cada encabezado es asociado a la columna correspondiente en el Treeview.
tree.heading("idEncuesta", text="ID")  # Encabezado para la columna ID
tree.heading("Edad", text="Edad")  # Encabezado para la columna Edad
tree.heading("Sexo", text="Sexo")  # Encabezado para la columna Sexo
tree.heading("BebidasSemana", text="Bebidas Semana")  # Encabezado para la columna BebidasSemana
tree.heading("CervezasSemana", text="Cervezas Semana")  # Encabezado para la columna CervezasSemana
tree.heading("BebidasFinSemana", text="Bebidas Fin de Semana")  # Encabezado para la columna BebidasFinSemana
tree.heading("BebidasDestiladasSemana", text="Bebidas Destiladas Semana")  # Encabezado para la columna BebidasDestiladasSemana
tree.heading("VinosSemana", text="Vinos Semana")  # Encabezado para la columna VinosSemana
tree.heading("PerdidasControl", text="Perdida de Control")  # Encabezado para la columna PerdidasControl
tree.heading("DiversionDependenciaAlcohol", text="Dependencia Diversión")  # Encabezado para la columna DiversionDependenciaAlcohol
tree.heading("ProblemasDigestivos", text="Problemas Digestivos")  # Encabezado para la columna ProblemasDigestivos
tree.heading("TensionAlta", text="Tensión Alta")  # Encabezado para la columna TensionAlta
tree.heading("DolorCabeza", text="Dolor de Cabeza")  # Encabezado para la columna DolorCabeza

# Empaquetar el Treeview en el interfaz gráfica
# El Treeview se ajusta a todo el espacio disponible y se añaden márgenes de 10 píxeles en todas las direcciones.
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica (Tkinter)
# Este bucle mantiene la ventana abierta y permite la interacción con la interfaz gráfica.
root.mainloop()
