# Generated by Django 4.2.7 on 2023-12-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_date', models.DateField()),
            ],
        ),
    ]