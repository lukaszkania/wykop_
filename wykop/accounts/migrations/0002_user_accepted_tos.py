# Generated by Django 2.1.7 on 2019-03-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_tos',
            field=models.IntegerField(default=0),
        ),
    ]
