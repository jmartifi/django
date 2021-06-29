# Generated by Django 3.2.3 on 2021-06-29 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_servicios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('tbes_cdg_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id estado')),
                ('tbes_sts_code', models.CharField(max_length=3, verbose_name='Código estado')),
                ('tbes_sts_nombre', models.CharField(max_length=255, verbose_name='Nombre estado')),
            ],
        ),
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('tbat_cdg_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id atención')),
                ('tbat_dsc_titulo', models.CharField(max_length=255, verbose_name='titulo')),
                ('tbat_fch_ingreso', models.DateField(max_length=255, verbose_name='titulo')),
                ('tbat_dsc_resena', models.TextField(max_length=255, verbose_name='titulo')),
                ('tbat_dsc_diagnostico', models.TextField(max_length=255, verbose_name='titulo')),
                ('tbat_img_imagena', models.ImageField(upload_to='galeria', verbose_name='titulo')),
                ('tbat_img_imagenb', models.ImageField(null=True, upload_to='galeria', verbose_name='titulo')),
                ('tbat_img_imagenc', models.ImageField(null=True, upload_to='galeria', verbose_name='titulo')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
                ('patente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicios')),
                ('sts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado')),
            ],
        ),
    ]
