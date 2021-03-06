# Generated by Django 2.2.11 on 2020-04-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=30)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('bank_name', models.TextField()),
            ],
        ),
    ]
