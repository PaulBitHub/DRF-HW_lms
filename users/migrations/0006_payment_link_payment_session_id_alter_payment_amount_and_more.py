# Generated by Django 5.1.4 on 2024-12-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Cсылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Id сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.PositiveIntegerField(
                help_text="Укажите сумму платежа", verbose_name="Сумма платежа"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты"),
        ),
    ]
