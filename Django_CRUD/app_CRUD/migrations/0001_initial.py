# Generated by Django 4.2.7 on 2023-11-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
