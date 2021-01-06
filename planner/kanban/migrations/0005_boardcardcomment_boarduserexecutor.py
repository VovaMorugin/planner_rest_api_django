# Generated by Django 3.1.5 on 2021-01-06 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanban', '0004_boardcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardUserExecutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban.boardcard', verbose_name='User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Board user executor',
                'verbose_name_plural': 'Board user executors',
                'db_table': 'board_user_executors',
            },
        ),
        migrations.CreateModel(
            name='BoardCardComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Message')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Time of creation')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban.boardcard', verbose_name='User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Board card comment',
                'verbose_name_plural': 'Board card comments',
                'db_table': 'board_card_comments',
            },
        ),
    ]
