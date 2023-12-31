# Generated by Django 4.2.6 on 2023-11-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_alter_log_card_id_alter_student_admission_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='card_id',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_id',
            field=models.CharField(default='0', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
