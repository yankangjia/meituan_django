# Generated by Django 2.2.9 on 2020-01-27 13:40

import apps.mtauth.models
from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False, verbose_name='用户表主键')),
                ('telephone', models.CharField(max_length=11, unique=True, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='邮箱')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('avatar', models.CharField(max_length=200, verbose_name='头像链接')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('is_staff', models.BooleanField(default=False, verbose_name='是否是员工')),
                ('is_merchant', models.BooleanField(default=False, verbose_name='是否是商家')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.mtauth.models.UserManager()),
            ],
        ),
    ]
