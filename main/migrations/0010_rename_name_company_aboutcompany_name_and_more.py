# Generated by Django 4.1.5 on 2023-02-21 04:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_course_location_cart_alter_category_posted_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutcompany',
            old_name='name_company',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 10, 2, 13, 983335)),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 10, 2, 14, 21094)),
        ),
    ]
