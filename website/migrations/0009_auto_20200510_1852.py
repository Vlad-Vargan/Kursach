# Generated by Django 2.1.7 on 2020-05-10 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_employee_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='username',
            new_name='login',
        ),
    ]
