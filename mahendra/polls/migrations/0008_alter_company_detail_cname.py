# Generated by Django 4.2.5 on 2023-09-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_company_detail_cemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_detail',
            name='Cname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
