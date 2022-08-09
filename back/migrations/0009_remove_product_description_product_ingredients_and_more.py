# Generated by Django 4.0.4 on 2022-08-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0008_alter_product_category_alter_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='Ingredients',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Instructions',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.IntegerField(default=70),
        ),
    ]