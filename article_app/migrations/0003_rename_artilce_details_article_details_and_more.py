# Generated by Django 4.1 on 2022-09-09 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0002_artilce_details_article_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='artilce_details',
            new_name='article_details',
        ),
        migrations.RenameModel(
            old_name='artilce_sale',
            new_name='article_sale',
        ),
    ]
