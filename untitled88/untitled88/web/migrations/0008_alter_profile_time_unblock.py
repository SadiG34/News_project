# Generated by Django 5.0.2 on 2024-02-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_profile_isblocked_profile_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_unblock',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время разблокировки'),
        ),
    ]