# Generated by Django 3.2.3 on 2021-06-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210628_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('tbse_cdg_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id servicio')),
                ('tbse_dsc_nombre', models.CharField(max_length=255, verbose_name='Nombre servicio')),
            ],
        ),
    ]