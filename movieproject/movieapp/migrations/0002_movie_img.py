# Generated by Django 4.2.7 on 2023-11-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='aaa', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
