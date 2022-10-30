# Generated by Django 4.1.2 on 2022-10-30 11:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]