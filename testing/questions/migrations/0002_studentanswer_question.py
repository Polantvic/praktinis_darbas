# Generated by Django 5.0.3 on 2024-03-25 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='studentanswers', to='questions.question', verbose_name='question'),
            preserve_default=False,
        ),
    ]
