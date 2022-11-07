# Generated by Django 4.1.3 on 2022-11-07 09:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, verbose_name='unique ID')),
                ('due_back', models.DateField(blank=True, null=True, verbose_name='due back')),
                ('status', models.CharField(choices=[('a', 'managed'), ('t', 'taken'), ('a', 'available'), ('r', 'reserved')], default='m', max_length=1, verbose_name='status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='book')),
            ],
        ),
    ]
