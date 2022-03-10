# Generated by Django 4.0.2 on 2022-02-26 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('litreview', '0004_alter_userfollows_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
