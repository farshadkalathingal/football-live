# Generated by Django 3.1.1 on 2020-09-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='collge',
            new_name='college',
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
