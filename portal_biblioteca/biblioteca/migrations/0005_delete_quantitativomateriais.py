# Generated by Django 5.1.2 on 2024-11-04 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_rename_qtdapostilas_quantitativomateriais_apostilas_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuantitativoMateriais',
        ),
    ]