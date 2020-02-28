# Generated by Django 2.2.7 on 2020-02-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_v1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='probability',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_order',
            field=models.IntegerField(null=True),
        ),
    ]
