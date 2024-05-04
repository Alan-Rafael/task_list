# Generated by Django 4.2.11 on 2024-04-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('data', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'A FAZER'), (2, 'FAZENDO'), (3, 'CONCLUIDO')])),
            ],
        ),
    ]