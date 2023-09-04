# Generated by Django 4.2.4 on 2023-09-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=150)),
                ('cor', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=150)),
                ('ano', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
                ('km', models.CharField(max_length=100)),
                ('passagem', models.CharField(max_length=100)),
                ('pagamento', models.CharField(max_length=100)),
            ],
        ),
    ]