# Generated by Django 3.2.9 on 2022-01-25 07:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityEvent',
            fields=[
                ('Event_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Eventname', models.CharField(max_length=100)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('City', models.CharField(max_length=50)),
                ('VenueAddress', models.TextField()),
                ('Description', models.TextField()),
                ('EventPic', models.ImageField(default='', max_length=255, upload_to='summercamp/event_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=45)),
                ('Phone', models.CharField(max_length=10)),
                ('Question', models.TextField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('Feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=45)),
                ('CampName', models.CharField(max_length=100)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('FeedbackText', models.TextField()),
                ('Rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('Summercamp_Id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=45)),
                ('CampName', models.CharField(max_length=50)),
                ('OwnerName', models.CharField(max_length=40)),
                ('CampEmailid', models.EmailField(max_length=45)),
                ('CampMobileno', models.CharField(max_length=10)),
                ('CampAddress', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program_detail',
            fields=[
                ('Program_Id', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=20)),
                ('Fees', models.CharField(max_length=30)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Description', models.TextField()),
                ('AgeGroup', models.CharField(max_length=20)),
                ('Summercamp_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summercamp.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_Id', models.CharField(max_length=30)),
                ('PostName', models.CharField(max_length=30)),
                ('No_ofseats', models.IntegerField()),
                ('LastDatetoapply', models.DateField()),
                ('Postdate', models.DateField(default=django.utils.timezone.now)),
                ('Description', models.TextField()),
                ('Summercamp_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summercamp.organizer')),
            ],
        ),
    ]
