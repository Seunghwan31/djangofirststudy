# Generated by Django 5.0.6 on 2024-05-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('content', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('like', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]