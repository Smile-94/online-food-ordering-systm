# Generated by Django 4.1.7 on 2023-03-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermessage',
            name='send_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]