# Generated by Django 4.0.5 on 2022-06-17 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fechadenac', models.DateField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
