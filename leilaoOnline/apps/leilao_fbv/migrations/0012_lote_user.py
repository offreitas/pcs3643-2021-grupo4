# Generated by Django 3.2.8 on 2021-10-09 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leilao_fbv', '0011_vendedor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
