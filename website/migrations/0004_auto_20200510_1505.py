# Generated by Django 2.1.7 on 2020-05-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200510_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='gender',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='surname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
