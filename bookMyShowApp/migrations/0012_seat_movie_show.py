# Generated by Django 4.1.4 on 2022-12-16 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookMyShowApp', '0011_remove_seat_movie_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='movie_show',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='bookMyShowApp.screenmovie'),
            preserve_default=False,
        ),
    ]