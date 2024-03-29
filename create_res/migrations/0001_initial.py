# Generated by Django 3.2 on 2024-03-01 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('middlename', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('emailaddress', models.EmailField(max_length=250)),
                ('gender', models.CharField(default='no', max_length=30)),
                ('user_name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('confirmpassword', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_res.register')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='update_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_obj', models.CharField(max_length=500)),
                ('mob_no', models.IntegerField()),
                ('skills', models.CharField(max_length=250)),
                ('projects', models.CharField(max_length=250)),
                ('tools', models.CharField(max_length=250)),
                ('achievements', models.CharField(max_length=250)),
                ('lan_knw', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_res.register')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('high_school', 'High School'), ('intermediate', 'Intermediate'), ('bachelors', "Bachelor's"), ('masters', "Master's"), ('phd', 'PhD')], max_length=100)),
                ('institution', models.CharField(max_length=255)),
                ('cgpa', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_res.register')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
