# Generated by Django 2.0.2 on 2018-04-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cancel',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
