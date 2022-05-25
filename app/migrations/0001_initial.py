# Generated by Django 3.2.5 on 2022-05-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='タイトル')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='サブタイトル')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('job', models.TextField(verbose_name='仕事')),
                ('introduction', models.TextField(verbose_name='自己紹介')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='linkedin')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='facebook')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram')),
                ('topimage', models.ImageField(upload_to='images', verbose_name='トップ画像')),
                ('subimage', models.ImageField(upload_to='images', verbose_name='サブ画像')),
            ],
        ),
    ]
