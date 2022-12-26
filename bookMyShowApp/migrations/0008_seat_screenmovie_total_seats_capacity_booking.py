# Generated by Django 4.1.4 on 2022-12-16 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookMyShowApp', '0007_screenmovie_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='screenmovie',
            name='total_seats_capacity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('seat', models.ManyToManyField(related_name='seats', to='bookMyShowApp.seat')),
                ('show_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookMyShowApp.screenmovie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]