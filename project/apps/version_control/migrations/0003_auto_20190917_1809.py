# Generated by Django 2.2.5 on 2019-09-17 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0002_auto_20190917_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environments', to='version_control.Client'),
        ),
    ]
