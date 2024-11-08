# Generated by Django 5.1.2 on 2024-11-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_delete_quantitativomateriais'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantitativoMateriais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livros', models.IntegerField()),
                ('tccs', models.IntegerField()),
                ('dissertacoes', models.IntegerField()),
                ('teses', models.IntegerField()),
                ('apostilas', models.IntegerField()),
                ('jornais', models.IntegerField()),
            ],
        ),
    ]