# Generated by Django 4.1.1 on 2022-09-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_remove_book_borrower_bookinstance_borrower"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("m", "Maintenance"),
                    ("o", "On loan"),
                    ("a", "Available"),
                    ("r", "Reserved"),
                ],
                default="m",
                help_text="Book availability",
                max_length=1,
            ),
        ),
    ]
