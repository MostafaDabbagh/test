# Generated by Django 4.0.2 on 2022-02-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_file2_bil_remove_uploadfile_bill_delete_bil2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Truck'), (4, 'SUV')])),
            ],
        ),
        migrations.RenameModel(
            old_name='File',
            new_name='Filee',
        ),
    ]