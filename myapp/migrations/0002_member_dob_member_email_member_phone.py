# Generated by Django 5.1.4 on 2024-12-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
