# Generated by Django 4.2 on 2023-05-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_email_url_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='url_score',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
