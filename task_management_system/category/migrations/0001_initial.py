# Generated by Django 4.2.7 on 2023-12-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=25)),
                ('task', models.ManyToManyField(to='task.taskmodel')),
            ],
        ),
    ]
