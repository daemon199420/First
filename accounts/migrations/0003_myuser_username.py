# Generated by Django 2.1.1 on 2018-09-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180925_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]