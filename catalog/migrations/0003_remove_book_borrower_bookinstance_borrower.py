# Generated by Django 4.1.1 on 2022-09-08 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0002_book_borrower"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="borrower",),
        migrations.AddField(
            model_name="bookinstance",
            name="borrower",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]