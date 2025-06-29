# Generated by Django 5.2.3 on 2025-06-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ism')),
                ('email', models.EmailField(max_length=254, verbose_name='Email manzilingiz')),
                ('subject', models.CharField(max_length=255, verbose_name='Mavzu')),
                ('message', models.TextField()),
            ],
        ),
    ]
