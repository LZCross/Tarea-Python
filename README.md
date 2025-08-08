# 🛠️ Proyecto CRUD en PHP con Pruebas Automatizadas (Selenium)

Este proyecto es un sistema **CRUD** (Crear, Leer, Actualizar, Eliminar) desarrollado en **PHP** con base de datos MySQL (XAMPP) y diseño con **Bootstrap**.  
Incluye **pruebas automatizadas** con **Python + Selenium** y un reporte HTML con capturas de cada paso.

---

## 📂 Estructura del proyecto

```
📦 tarea4
 ┣ 📜 index.php
 ┣ 📜 agregar.php
 ┣ 📜 editar.php
 ┣ 📜 eliminar.php
 ┣ 📜 conexion.php
 ┣ 📂 capturas
 ┃ ┣ 01_inicio.png
 ┃ ┣ 02_usuario_creado.png
 ┃ ┣ 03_usuario_editado.png
 ┃ ┣ 04_usuario_eliminado.png
 ┃ ┗ 05_error_formulario_vacio.png
 ┣ 📂 selenium-tests
 ┃ ┗ selenium_crud_tests.py
 ┣ 📜 reporte_pruebas_selenium.html
 ┗ 📜 README.md
```

---

## 🚀 Instalación y uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/proyecto-crud-selenium.git
cd proyecto-crud-selenium
```

### 2️⃣ Configurar base de datos
- Importa el archivo SQL en **phpMyAdmin** para crear la base de datos y tabla.
- Ajusta las credenciales en `conexion.php`.

Ejemplo:
```php
$host = "localhost";
$usuario = "root";
$clave = "";
$baseDatos = "crud";
```

### 3️⃣ Iniciar servidor local
Si usas XAMPP:
- Inicia Apache y MySQL
- Coloca el proyecto en `C:\xampp\htdocs\tarea4`
- Abre en el navegador:  
  [http://localhost/tarea4](http://localhost/tarea4)

---

## 🤖 Pruebas Automatizadas (Selenium)

### 1️⃣ Requisitos
- Python 3.x
- Selenium
- ChromeDriver compatible con tu versión de Chrome

Instalar dependencias:
```bash
pip install selenium
```

### 2️⃣ Ejecutar pruebas
```bash
cd selenium-tests
python selenium_crud_tests.py
```

Esto:
- Crea un usuario
- Lo edita
- Lo elimina
- Realiza una prueba negativa con campos vacíos
- Genera capturas en `/capturas`
- Genera un reporte en `reporte_pruebas_selenium.html`

---

## 📊 Reporte HTML
El archivo `reporte_pruebas_selenium.html` contiene:
- Evidencias gráficas de cada prueba
- Resultados de ejecución
- Estado de aprobación de todas las pruebas

---

## 👨‍💻 Tecnologías usadas
- **PHP 8.2**
- **MySQL / phpMyAdmin**
- **Bootstrap 5**
- **Python 3 + Selenium**
- **ChromeDriver**

---

## 📜 Licencia
Este proyecto es de uso libre con fines educativos.
