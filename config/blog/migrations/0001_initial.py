# Generated by Django 3.2.19 on 2023-05-06 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(choices=[('p', 'published'), ('d', 'draft')], max_length=1)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]