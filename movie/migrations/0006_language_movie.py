# Generated by Django 3.0 on 2020-08-28 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('duration', models.CharField(max_length=100, null=True)),
                ('director', models.CharField(max_length=100, null=True)),
                ('casting', models.CharField(max_length=100, null=True)),
                ('release_date', models.DateField(null=True)),
                ('premier_date', models.DateField(null=True)),
                ('trailer', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('certificate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Certificate')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Language')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Movie_Type')),
            ],
        ),
    ]
