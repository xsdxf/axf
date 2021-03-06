# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_homemainshow_homemustbuy_homeshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=32)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.CharField(max_length=100)),
                ('specifics', models.CharField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('marketprice', models.CharField(max_length=32)),
                ('categoryid', models.CharField(max_length=16)),
                ('childcid', models.CharField(max_length=16)),
                ('childcidname', models.CharField(max_length=32)),
                ('dealerid', models.CharField(max_length=32)),
                ('storenums', models.CharField(max_length=32)),
                ('productnum', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='MarketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=16)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
