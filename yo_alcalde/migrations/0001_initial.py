# Generated by Django 5.0.1 on 2024-04-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vecino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apaterno', models.CharField(max_length=100)),
                ('amaterno', models.CharField(max_length=100)),
                ('nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]
