# Generated by Django 3.1.7 on 2021-04-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]