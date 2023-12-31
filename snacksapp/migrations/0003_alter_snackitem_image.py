# Generated by Django 4.2.5 on 2023-09-17 02:42

from django.db import migrations, models
import storages.backends.s3


class Migration(migrations.Migration):

    dependencies = [
        ('snacksapp', '0002_snackimage_snackitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snackitem',
            name='image',
            field=models.ImageField(default='www.google.com', storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
    ]
