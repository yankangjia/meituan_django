# Generated by Django 2.2.9 on 2020-02-05 14:42

import apps.meituan.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meituan', '0003_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(default=apps.meituan.models.generate_order_uid, max_length=100, primary_key=True, serialize=False, verbose_name='订单id')),
                ('pay_method', models.SmallIntegerField(choices=[(0, '未选择'), (1, '微信支付'), (2, '支付宝')], default=0, verbose_name='支付方式')),
                ('order_status', models.SmallIntegerField(choices=[(1, '待支付'), (2, '待发货'), (3, '配送中'), (4, '待评价'), (5, '已完成')], default=1, verbose_name='订单状态')),
                ('goods_count', models.SmallIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='成交总价')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meituan.UserAddress', verbose_name='地址')),
                ('goods_list', models.ManyToManyField(to='meituan.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
    ]
