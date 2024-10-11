# Proyecto de Biblioteca y API de Tareas

## Requisitos

- Python 3.x
- Django 3.x o superior
- MySQL
- Django REST Framework

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Eldavi5/biblioteca.git
   cd proyecto_biblioteca_api
   ```

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Configura la base de datos en `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nombre_de_tu_base_de_datos',
           'USER': 'tu_usuario_mysql',
           'PASSWORD': 'tu_contraseña_mysql',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. Ejecuta las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Tareas

- **Crear Tarea**: `POST /api/tareas/`
- **Leer Tareas**: `GET /api/tareas/`
- **Actualizar Tarea**: `PUT /api/tareas/<id>/`
- **Eliminar Tarea**: `DELETE /api/tareas/<id>/`

### Funciones Adicionales

- **Contar Palabras**: `POST /api/contar_palabras/`

  - **Body**:
    ```json
    {
      "archivo": "ruta/al/archivo.txt"
    }
    ```
  - **Respuesta**:
    ```json
    {
      "cantidad_palabras": 123
    }
    ```

- **Ordenar Lista**: `POST /api/ordenar_lista/`
  - **Body**:
    ```json
    {
      "lista_numeros": [5, 2, 9, 1, 5, 6]
    }
    ```
  - **Respuesta**:
    ```json
    {
      "lista_ordenada": [1, 2, 5, 5, 6, 9]
    }
    ```

## Notas Adicionales

- Asegúrate de que el archivo que deseas procesar en la función de contar palabras esté disponible en el servidor y proporciona la ruta correcta en el cuerpo de la solicitud.
- Para probar las API puedes utilizar herramientas como Postman o cURL.
