# Generated by Django 3.2.8 on 2021-10-15 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leilao_fbv', '0013_auto_20211015_2137'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comprador',
        ),
        migrations.DeleteModel(
            name='CompradorDAO',
        ),
        migrations.DeleteModel(
            name='Leiloeiro',
        ),
        migrations.DeleteModel(
            name='LeiloeiroDAO',
        ),
        migrations.DeleteModel(
            name='Lote',
        ),
        migrations.DeleteModel(
            name='LoteDAO',
        ),
        migrations.DeleteModel(
            name='Relatorio',
        ),
    ]
