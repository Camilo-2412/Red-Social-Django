# Generated by Django 3.1.6 on 2021-02-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]
