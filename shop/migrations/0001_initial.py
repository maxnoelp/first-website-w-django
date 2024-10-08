# Generated by Django 5.1.1 on 2024-09-25 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('beschreibung', models.TextField(blank=True, null=True)),
                ('preis', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='bestellung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestelldatum', models.DateTimeField(auto_now_add=True)),
                ('erledigt', models.BooleanField(blank=True, default=False, null=True)),
                ('auftragsId', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='bestellteArtikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menge', models.IntegerField(blank=True, default=0, null=True)),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('artikel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.artikel')),
                ('Bestellung', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.bestellung')),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('benutzer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bestellung',
            name='kunde',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.kunde'),
        ),
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('plz', models.CharField(max_length=200, null=True)),
                ('stadt', models.CharField(max_length=200, null=True)),
                ('land', models.CharField(max_length=200, null=True)),
                ('datum', models.DateTimeField(auto_now_add=True)),
                ('Bestellung', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.bestellung')),
                ('kunde', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.kunde')),
            ],
        ),
    ]
