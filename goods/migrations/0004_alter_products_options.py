# Generated by Django 5.1.4 on 2025-01-05 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]