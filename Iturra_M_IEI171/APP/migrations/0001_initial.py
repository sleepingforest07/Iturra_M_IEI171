# Generated by Django 4.2.7 on 2023-11-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios_Del_Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Socio', models.CharField(max_length=50)),
                ('Fecha_Incorporacion', models.DateField()),
                ('Año_nacimiento', models.DateField()),
                ('Telefono', models.CharField(max_length=30)),
                ('Correo_Electronico', models.EmailField(max_length=254)),
                ('Sexo', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=200)),
            ],
        ),
    ]
