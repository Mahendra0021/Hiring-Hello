# Generated by Django 4.2.5 on 2023-09-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_company_detail_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detail',
            name='CEmail',
            field=models.EmailField(max_length=500),
        ),
    ]
