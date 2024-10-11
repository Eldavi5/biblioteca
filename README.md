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

## Información del Desarrollador

- **Último Empleo**: LOOP CONEXIÓN EMPRESARIAL
- **Herramientas Conocidas**:
  - Django
  - Python
  - ReactJS
  - React Native
  - GitHub
  - GitLab
  - Docker
  - PostgreSQL
- **Edad**: 24 años
- **Estado Civil**: Soltero
- **Estado**: Estado de México
- **Municipio**: Tlalnepantla de Baz
- **Cualidades**:
  - **Proactivo**: Siempre busco formas de mejorar los procesos y contribuir al éxito del equipo.
  - **Adaptable**: Puedo trabajar eficazmente en entornos dinámicos y aprender rápidamente nuevas tecnologías.
  - **Orientado a resultados**: Me enfoco en cumplir objetivos y superar expectativas en cada proyecto.
  - **Colaborativo**: Disfruto trabajando en equipo y creo que las mejores soluciones surgen de la colaboración.
  - **Habilidades de comunicación**: Puedo transmitir ideas complejas de manera clara y efectiva a diferentes audiencias.

### Preguntas Frecuentes

1. **¿Por qué te tienen que contratar?**

   - Me considero un candidato ideal por mi sólida experiencia en desarrollo de software, especialmente con Django y React. He trabajado en proyectos desafiantes donde he demostrado mi capacidad para resolver problemas complejos y entregar soluciones efectivas en plazos ajustados. Además, mi enfoque colaborativo y habilidades interpersonales me permiten integrarme rápidamente en cualquier equipo y contribuir al logro de los objetivos comunes.

2. **¿Qué te motiva en tu vida?**
   - Estoy motivado por el deseo de aprender y crecer continuamente, tanto profesional como personalmente. Me apasiona enfrentar nuevos desafíos y superar obstáculos, ya sea a través de proyectos innovadores en tecnología o mediante el aprendizaje de nuevas habilidades. Además, creo que hacer un impacto positivo en mi entorno y ayudar a otros a alcanzar su potencial es una de mis mayores motivaciones.

### Preguntas Técnicas

#### Django

1. **¿Qué es Django y por qué se usa?**

   - Django es un framework de desarrollo web de alto nivel para Python que permite la creación rápida de aplicaciones web seguras y escalables. Se utiliza por su enfoque en la reutilización de componentes, la facilidad de desarrollo y su capacidad para gestionar tareas comunes en el desarrollo web, como autenticación y administración de bases de datos.

2. **Explica brevemente el patrón MVC (Modelo-Vista-Controlador) y cómo se implementa en Django.**

   - El patrón MVC es una forma de estructurar aplicaciones en tres componentes principales:
     - **Modelo**: La capa que maneja la lógica de datos y la interacción con la base de datos.
     - **Vista**: La capa que se encarga de la presentación de la información al usuario.
     - **Controlador**: La capa que recibe las entradas del usuario y llama a las vistas y modelos apropiados.
       En Django, se utiliza un enfoque llamado MTV (Modelo-Template-Vista), donde:
   - **Modelo**: Define la estructura de los datos.
   - **Template**: Se encarga de la presentación (equivalente a la vista).
   - **Vista**: Maneja la lógica de negocio y conecta los modelos con los templates.

3. **¿Qué es un modelo en Django y cómo se define?**

   - Un modelo en Django es una representación de una tabla de base de datos en forma de clase. Se define creando una subclase de `django.db.models.Model`, donde cada atributo de la clase representa un campo de la tabla. Ejemplo:

   ```python
   from django.db import models

   class Libro(models.Model):
       titulo = models.CharField(max_length=200)
       autor = models.CharField(max_length=100)
       fecha_publicacion = models.DateField()
   ```
