# Generated by Django 4.0.2 on 2022-02-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_file2_bil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bil',
            name='name',
            field=models.TextField(),
        ),
    ]