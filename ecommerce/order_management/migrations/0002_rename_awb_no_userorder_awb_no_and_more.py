# Generated by Django 4.2.14 on 2024-08-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='AWB_NO',
            new_name='awb_no',
        ),
        migrations.AlterField(
            model_name='userorder',
            name='grand_total',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Grand Total'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='shipping_charges',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Shipping Charges'),
        ),
    ]
