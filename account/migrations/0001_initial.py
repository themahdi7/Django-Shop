# Generated by Django 4.2.1 on 2023-06-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن')),
                ('fullname', models.CharField(max_length=50, verbose_name='نام کامل')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name=' ادرس ایمیل')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
        ),
    ]
