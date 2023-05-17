# Generated by Django 4.2 on 2023-05-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_commande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]