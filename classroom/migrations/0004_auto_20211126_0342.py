# Generated by Django 3.2.8 on 2021-11-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20211125_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmission',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examsubmission',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
