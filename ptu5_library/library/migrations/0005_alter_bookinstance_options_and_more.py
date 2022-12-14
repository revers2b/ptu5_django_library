# Generated by Django 4.1.3 on 2022-11-08 07:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_bookinstance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='unique ID'),
        ),
    ]
