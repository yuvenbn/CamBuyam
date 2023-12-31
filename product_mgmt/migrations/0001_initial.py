# Generated by Django 4.2.1 on 2023-06-27 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(max_length=100)),
                ('market_location', models.CharField(max_length=100)),
                ('gmap_location_link', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shed_number', models.CharField(default='', max_length=15)),
                ('store_name', models.CharField(max_length=100)),
                ('store_location', models.CharField(max_length=100)),
                ('gmap_location_link', models.CharField(max_length=1000, null=True)),
                ('market_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_mgmt.market')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account_mgmt.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='product_photos/')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=100)),
                ('measurement_unit', models.CharField(max_length=100)),
                ('approval_status', models.CharField(default='unverified', max_length=20)),
                ('uploaded_at', models.DateField(auto_now_add=True, null=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account_mgmt.customadmin')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account_mgmt.seller')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_mgmt.store')),
            ],
        ),
    ]
