# Generated by Django 5.1.3 on 2024-11-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='p_email',
            field=models.EmailField(max_length=254),
        ),
    ]
