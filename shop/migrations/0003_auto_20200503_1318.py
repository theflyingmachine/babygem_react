# Generated by Django 3.0.5 on 2020-05-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200503_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='custID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='imgurl',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
