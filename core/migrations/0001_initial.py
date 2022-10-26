# Generated by Django 4.0.4 on 2022-04-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='companies')),
                ('short_description', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True, max_length=350, null=True)),
                ('photo', models.ImageField(upload_to='general-link')),
                ('short_description', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, choices=[('Uzbek', "O'zbek tili"), ('Russian', 'Rus tili'), ('English', 'Ingliz tili'), ('Other', 'Boshqa'), ('Several', 'Bir nechta')], max_length=50, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.section')),
            ],
        ),
    ]
