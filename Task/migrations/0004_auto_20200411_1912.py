# Generated by Django 2.2.11 on 2020-04-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20200411_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchs',
            old_name='bank',
            new_name='bank_id',
        ),
    ]
