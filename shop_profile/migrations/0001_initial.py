# Generated by Django 3.1.7 on 2021-04-08 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_registered_name', models.CharField(max_length=100)),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_user_name', models.CharField(max_length=10, unique=True)),
                ('shop_owner_name', models.CharField(max_length=150)),
                ('shop_address', models.CharField(max_length=100)),
                ('shop_warehouse_address', models.CharField(max_length=100)),
                ('shop_returned_address', models.CharField(max_length=100)),
                ('shop_category', models.CharField(max_length=100)),
                ('shop_detail_description', models.CharField(max_length=1000)),
                ('shop_pan_card', models.ImageField(upload_to='')),
                ('shop_phone_number', models.BigIntegerField()),
                ('shop_owner_phone_number', models.BigIntegerField()),
                ('is_verified', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
