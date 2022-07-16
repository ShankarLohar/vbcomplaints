# Generated by Django 4.0.6 on 2022-07-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_complain_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=122)),
                ('regno', models.CharField(max_length=10)),
                ('hostelGender', models.CharField(max_length=20)),
                ('hostelBlock', models.CharField(max_length=10)),
                ('roomNo', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
