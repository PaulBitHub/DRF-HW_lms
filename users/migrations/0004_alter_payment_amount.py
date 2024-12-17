# Generated by Django 5.1.4 on 2024-12-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_payment_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=20, verbose_name="Сумма"
            ),
        ),
    ]