# Generated by Django 3.0.8 on 2020-08-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200812_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='category',
            name='slug_field',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='slug_field',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
