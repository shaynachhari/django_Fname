# Generated by Django 4.0.1 on 2022-01-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('roll', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('meassge', models.TextField()),
            ],
        ),
    ]
