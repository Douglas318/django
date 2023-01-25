# Generated by Django 4.1.5 on 2023-01-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportador', '0003_marcozero_areadecorte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cnpj',
            field=models.CharField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nome',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='marcozero',
            name='endereco',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='marcozero',
            name='lat_long',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
