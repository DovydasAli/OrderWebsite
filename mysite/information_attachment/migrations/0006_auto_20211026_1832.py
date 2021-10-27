# Generated by Django 3.2.8 on 2021-10-26 15:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('information_attachment', '0005_auto_20211026_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageorderproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='imageorderproduct',
            name='order_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_attachment.orderproduct'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imageorder',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique order picture ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='imageorderproduct',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique product picture ID', primary_key=True, serialize=False),
        ),
    ]
