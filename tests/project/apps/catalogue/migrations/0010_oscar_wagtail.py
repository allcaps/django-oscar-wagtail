# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('catalogue', '0009_slugfield_noop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='numchild',
        ),
        migrations.RemoveField(
            model_name='category',
            name='path',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Description'),
        ),
    ]