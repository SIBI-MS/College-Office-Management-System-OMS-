# Generated by Django 4.2.6 on 2023-11-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_alter_student_admission_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='card_id',
            field=models.CharField(max_length=20, default='0'),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.CharField(max_length=20, blank=True, null=True)
        ),
        migrations.AlterField(
            model_name='student',
            name='card_id',
            field=models.CharField(max_length=20, primary_key=True, default='0'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10, default='0'),
        ),
    ]
