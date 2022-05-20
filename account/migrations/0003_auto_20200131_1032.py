# Generated by Django 3.0 on 2020-01-31 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Products')),
            ],
        ),
    ]