# Generated by Django 4.2.4 on 2023-10-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_log_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='time_spend',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
