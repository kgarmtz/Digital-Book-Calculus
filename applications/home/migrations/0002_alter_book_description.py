# Generated by Django 3.2.7 on 2021-09-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
    ]