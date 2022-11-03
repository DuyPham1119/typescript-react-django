# Generated by Django 4.1.1 on 2022-11-03 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=50, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('latest_chapter', models.IntegerField(blank=True, default=0, null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('ONGOING', 'ongoing'), ('COMPLETED', 'completed')], default='ONGOING', max_length=250)),
                ('url', models.CharField(max_length=250, null=True)),
                ('total_view', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.author')),
            ],
            options={
                'ordering': ['-updated_date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('view', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='book.genre'),
        ),
    ]
