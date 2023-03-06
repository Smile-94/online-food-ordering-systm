# Generated by Django 4.1.7 on 2023-03-05 21:25

import authority.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authority', '0003_delete_customermessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=10)),
                ('sort_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to=authority.utils.category_directory_path)),
            ],
        ),
    ]