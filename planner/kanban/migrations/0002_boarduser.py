# Generated by Django 3.1.5 on 2021-01-05 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_owner', models.BooleanField(default=False, verbose_name='Board owner')),
                ('is_read_only', models.BooleanField(default=False, verbose_name='Board can be modified')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban.board', verbose_name='Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Board user',
                'verbose_name_plural': 'Board users',
                'db_table': 'board_users',
            },
        ),
    ]
