# Generated by Django 5.1.1 on 2024-09-26 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proprietario',
            old_name='tipo_vaga',
            new_name='tipo_prop',
        ),
    ]