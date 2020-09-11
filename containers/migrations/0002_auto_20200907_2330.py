# Generated by Django 3.0.7 on 2020-09-07 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('length', models.CharField(blank=True, max_length=10)),
                ('width', models.CharField(blank=True, max_length=10)),
                ('height', models.CharField(blank=True, max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('category', models.CharField(blank=True, max_length=20)),
                ('in_container', models.IntegerField()),
                ('purpose', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='container',
            name='height',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='container',
            name='length',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='container',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='width',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
