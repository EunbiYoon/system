# Generated by Django 4.1.7 on 2023-04-28 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '1) Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '3) Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '2) Posts'},
        ),
    ]
