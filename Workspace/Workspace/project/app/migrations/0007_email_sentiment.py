# Generated by Django 4.2 on 2023-05-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_email_sentiment_email_anger_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='sentiment',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
