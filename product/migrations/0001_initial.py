# Generated by Django 3.2.6 on 2021-08-18 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_pice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_weight', models.IntegerField()),
                ('date_time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
