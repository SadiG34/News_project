# Generated by Django 5.0.2 on 2024-02-28 17:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_comment_news_alter_comment_text_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Добавить пользователя',
            },
        ),
        migrations.CreateModel(
            name='FavoriteNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.news', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'избранная новость',
                'verbose_name_plural': 'избранные новости',
            },
        ),
    ]
