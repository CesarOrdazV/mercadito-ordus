# Generated by Django 4.1.6 on 2023-02-14 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='agregado_por',
            new_name='added',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='fecha',
            new_name='date',
        ),
    ]