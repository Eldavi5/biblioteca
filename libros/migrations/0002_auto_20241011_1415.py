# libros/migrations/0002_auto_create_usuarios.py
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial')
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                email VARCHAR(100),
                fecha_de_registro DATE
            );
        """),
        migrations.RunSQL("""
            INSERT INTO Usuarios (nombre, email, fecha_de_registro)
            VALUES
                ('Juan Pérez', 'juan@example.com', '2023-01-10'),
                ('María Gómez', 'maria@example.com', '2023-03-15'),
                ('Carlos Ruiz', 'carlos@example.com', '2023-05-20');
        """),
    ]
