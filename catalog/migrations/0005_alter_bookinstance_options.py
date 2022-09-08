# Generated by Django 4.1.1 on 2022-09-08 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_bookinstance_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": (("can_mark_returned", "Set book as returned"),),
            },
        ),
    ]
