# Generated by Django 4.0.1 on 2022-01-19 11:04

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empcode', models.IntegerField()),
                ('Username', models.CharField(default='', max_length=50)),
                ('Password', models.CharField(default='', max_length=50)),
                ('is_active', models.IntegerField(null=True)),
            ],
            managers=[
                ('EmpAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
