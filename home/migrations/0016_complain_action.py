# Generated by Django 4.0.6 on 2022-07-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_complain_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='action',
            field=models.CharField(choices=[('Forwarded to Electrician', 'Forwarded to Electrician'), ('Forwarded to Hostel Warden', 'Forwarded to Hostel Warden'), ('Forwarded to Cleaning Staff', 'Forwarded to Cleaning Staff'), ('Forwarded to Security', 'Forwarded to Security')], default='No Action Taken', max_length=50),
        ),
    ]
