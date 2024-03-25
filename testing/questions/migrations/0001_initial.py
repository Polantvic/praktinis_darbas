# Generated by Django 5.0.3 on 2024-03-25 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(db_index=True, max_length=500, verbose_name='text')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(db_index=True, max_length=500, verbose_name='text')),
                ('choice', models.BooleanField(db_index=True, default=False, verbose_name='choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questions.question', verbose_name='question')),
            ],
            options={
                'verbose_name': 'option',
                'verbose_name_plural': 'options',
            },
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentanswers', to='questions.option', verbose_name='option')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentanswers', to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
            options={
                'verbose_name': 'studentanswer',
                'verbose_name_plural': 'studentanswers',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='description')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to=settings.AUTH_USER_MODEL, verbose_name='lecturer')),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'tests',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.test', verbose_name='test'),
        ),
    ]
