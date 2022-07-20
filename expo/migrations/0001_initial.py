# Generated by Django 4.0.6 on 2022-07-19 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('creation_date', models.DateField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ExpoDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('artworks', models.ManyToManyField(to='expo.artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('uri', models.CharField(max_length=255)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expo.artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Expo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('dates', models.ManyToManyField(to='expo.expodate')),
                ('portfolios', models.ManyToManyField(to='expo.portfolio')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='authors',
            field=models.ManyToManyField(to='expo.author'),
        ),
    ]
