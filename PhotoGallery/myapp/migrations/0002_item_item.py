# Generated by Django 3.1.7 on 2021-04-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]