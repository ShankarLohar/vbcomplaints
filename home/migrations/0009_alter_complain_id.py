# Generated by Django 4.0.6 on 2022-07-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_complain_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='id',
            field=models.CharField(default='VITB<django.db.models.fields.CharField><django.db.models.fields.DateField>', max_length=100, primary_key=True, serialize=False),
        ),
    ]
