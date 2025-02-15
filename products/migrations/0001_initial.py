# Generated by Django 5.1.1 on 2024-10-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('active', models.BooleanField()),
                ('datetime_created', models.DateTimeField()),
                ('datetime_modified', models.DateTimeField()),
            ],
        ),
    ]
