# Generated by Django 3.2.7 on 2021-09-06 04:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('image', models.FileField(upload_to='book', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='Cover')),
                ('color', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('yellow', 'yellow'), ('green', 'green')], max_length=20, verbose_name='Color')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.book')),
            ],
        ),
    ]
