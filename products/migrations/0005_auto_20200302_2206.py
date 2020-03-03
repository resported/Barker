# Generated by Django 3.0.3 on 2020-03-02 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200302_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='title',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='products.Gender'),
        ),
    ]
