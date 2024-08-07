# Generated by Django 5.0.6 on 2024-06-26 02:59

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
                ('tax_code', models.CharField(max_length=100, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('image', models.ImageField(unique=True, upload_to='assets/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
