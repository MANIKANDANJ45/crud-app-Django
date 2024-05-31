# Generated by Django 4.2.13 on 2024-05-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_person_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='role1',
            new_name='role',
        ),
        migrations.AddField(
            model_name='person',
            name='salary',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]