# Hito 2 1 Trimestre Sistemas de Gestion Empresarial Álvaro López Juara
## Análisis del Consumo de Alcohol y su Impacto en la Salud

### Introducción
El consumo de alcohol y sus efectos en la salud representan un desafío significativo para investigadores y responsables de políticas de salud pública. Este proyecto tiene como objetivo analizar los patrones de consumo de alcohol y su relación con factores demográficos y de salud. Al estudiar los datos sobre el consumo semanal de bebidas alcohólicas como cervezas, vinos y destilados, junto con información de edad y género, buscamos identificar comportamientos de riesgo y posibles áreas de intervención.

El objetivo principal es proporcionar herramientas analíticas y visualizaciones que apoyen decisiones basadas en datos.

---

### Características Principales
1. **Base de Datos**:  
   - Registros de encuestas con datos demográficos y patrones de consumo de alcohol.  
   - Cada registro cuenta con un identificador único y autoincremental para facilitar su manejo.  

2. **Interfaz Gráfica de Usuario (GUI)**:  
   - Diseñada con `tkinter`, ofrece una experiencia interactiva y fácil de usar.  
   - Permite gestionar y consultar los datos almacenados en la base de datos MySQL.  

3. **Visualización de Datos**:  
   - Utiliza `matplotlib` y `seaborn` para crear gráficos visualmente atractivos que destacan tendencias y patrones clave.

---

### Tecnologías y Librerías
Este proyecto utiliza las siguientes tecnologías y librerías:

- **tkinter**:
  - `messagebox`: Para mensajes emergentes (alertas y errores).
  - `Toplevel`: Ventanas secundarias dentro de la aplicación.
  - `ttk`: Widgets mejorados como tablas y comboboxes.
- **MySQL Connector**: Para la conexión y manipulación de la base de datos `ENCUESTAS`.
- **Pandas**: Para el análisis y manejo de datos tabulares.
- **Matplotlib.pyplot**: Para la generación de gráficos basados en los datos analizados.
- **Seaborn**: Para gráficos estadísticos detallados y estilizados.

---

### Función Principal: Conexión a la Base de Datos
La función de conexión establece una relación con la base de datos `ENCUESTAS` en un servidor MySQL. Credenciales utilizadas:

- **Host**: `localhost`
- **Usuario**: `root`
- **Contraseña**: `campusfp`
- **Base de Datos**: `ENCUESTAS`

En caso de error (como credenciales incorrectas o problemas de conexión), la aplicación notificará al usuario mediante mensajes claros y detallados.

---

### Estructura del Proyecto
1. **Base de Datos**:
   - Diseñada para optimizar la gestión de registros y asegurar que cada entrada sea única.

2. **Interfaz Gráfica**:
   - Intuitiva, con funcionalidades para consultar, analizar y visualizar los datos.

3. **Gráficos y Tablas**:
   - Representación clara y eficiente de tendencias y patrones clave.

---

### Instalación de Dependencias
Antes de ejecutar la aplicación, asegúrate de instalar las librerías necesarias. Sigue estos pasos en la terminal:

1. Asegúrate de tener instalado [Python 3](https://www.python.org/downloads/).
2. Instala las librerías requeridas ejecutando el siguiente comando en la terminal:

   ```bash
   pip install tkinter mysql-connector-python pandas matplotlib seaborn

## Repositorio
Encuentra el código fuente y documentación completa en [GitHub](https://github.com/AlvaroLopez31/Hito2_1Trim_SGE_ALJ.git).

---

Este proyecto fue desarrollado como parte del Hito 2 del 1er Trimestre en la asignatura Sistemas de Gestion Empresarion por Álvaro López Juara.





