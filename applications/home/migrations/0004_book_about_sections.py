# Generated by Django 3.2.7 on 2021-09-22 04:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210906_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='about_sections',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='About Section'),
        ),
    ]
