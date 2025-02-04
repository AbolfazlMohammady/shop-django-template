# Generated by Django 5.1.1 on 2024-10-20 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_size_alter_product_weight_delete_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='color',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.discount'),
        ),
    ]
