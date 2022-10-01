# Generated by Django 4.1.1 on 2022-10-01 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalBackend.medico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
