# Generated by Django 4.1.5 on 2023-02-23 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_siteuser_alter_category_posted_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 16, 42, 38, 613119)),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 16, 42, 38, 697838)),
        ),
        migrations.CreateModel(
            name='WishItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(blank=True, max_length=200)),
                ('status', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
    ]
