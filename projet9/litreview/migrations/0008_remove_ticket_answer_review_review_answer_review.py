# Generated by Django 4.0.2 on 2022-03-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litreview', '0007_remove_review_answer_review_ticket_answer_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='answer_review',
        ),
        migrations.AddField(
            model_name='review',
            name='answer_review',
            field=models.BooleanField(default=False),
        ),
    ]
