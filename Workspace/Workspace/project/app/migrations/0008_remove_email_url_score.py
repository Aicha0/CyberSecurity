# Generated by Django 4.2 on 2023-05-13 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_email_sentiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='url_score',
        ),
    ]
