# Generated by Django 3.2.9 on 2022-01-28 17:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('summercamp', '0003_alter_program_detail_summercamp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_detail',
            name='Description',
            field=models.TextField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='program_detail',
            name='EndDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='program_detail',
            name='StartDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
