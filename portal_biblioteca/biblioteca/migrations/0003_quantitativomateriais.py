# Generated by Django 5.1.2 on 2024-11-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_tcc'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantitativoMateriais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtdLivros', models.IntegerField()),
                ('qtdTCCs', models.IntegerField()),
                ('qtdDissertacoes', models.IntegerField()),
                ('qtdTeses', models.IntegerField()),
                ('qtdApostilas', models.IntegerField()),
                ('qtdJornais', models.IntegerField()),
            ],
        ),
    ]
