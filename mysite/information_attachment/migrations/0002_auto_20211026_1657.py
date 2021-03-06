# Generated by Django 3.2.8 on 2021-10-26 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information_attachment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='picture',
            field=models.ImageField(default='default.png', null=True, upload_to='product_pictures'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(help_text='Enter order number', max_length=200, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='information_attachment.order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='picture',
            field=models.ImageField(default='default.png', null=True, upload_to='product_pictures'),
        ),
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.CharField(help_text='Enter product number', max_length=200, verbose_name='Number'),
        ),
    ]
