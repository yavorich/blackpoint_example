# Generated by Django 5.1.3 on 2024-11-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0008_alter_subscriptionpayment_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("user_agreement", "Пользовательское соглашение"),
                            ("public_offer", "Публичная оферта"),
                            (
                                "privacy_policy",
                                "Политика обработки персональных данных",
                            ),
                        ],
                        verbose_name="Тип документа",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True, null=True, upload_to="", verbose_name="Файл"
                    ),
                ),
            ],
            options={
                "verbose_name": "документ",
                "verbose_name_plural": "Документы",
            },
        ),
    ]
