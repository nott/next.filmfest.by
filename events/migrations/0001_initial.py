# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-14 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('cpm_data', '0011_add_jury_data_to_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),  # noqa: E501
                ('starts_at', models.DateTimeField(db_index=True)),
                ('name_en', models.CharField(max_length=1000)),
                ('name_be', models.CharField(max_length=1000)),
                ('name_ru', models.CharField(max_length=1000)),
                ('description_en', wagtail.wagtailcore.fields.RichTextField(default='')),  # noqa: E501
                ('description_be', wagtail.wagtailcore.fields.RichTextField(default='')),  # noqa: E501
                ('description_ru', wagtail.wagtailcore.fields.RichTextField(default='')),  # noqa: E501
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FilmProgram',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),  # noqa: E501
                ('section', models.IntegerField(choices=[(1, 'Fiction'), (2, 'Animation'), (3, 'Documentary'), (4, 'Experimental')])),  # noqa: E501
                ('name_en', models.CharField(max_length=1000)),
                ('name_be', models.CharField(max_length=1000)),
                ('name_ru', models.CharField(max_length=1000)),
                ('description_en', wagtail.wagtailcore.fields.RichTextField(default='')),  # noqa: E501
                ('description_be', wagtail.wagtailcore.fields.RichTextField(default='')),  # noqa: E501
                ('description_ru', wagtail.wagtailcore.fields.RichTextField(default='')),  # noqa: E501
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FilmProgramRelatedFilm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),  # noqa: E501
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cpm_data.Film')),  # noqa: E501
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_films', to='events.FilmProgram')),  # noqa: E501
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.FilmProgram'),  # noqa: E501
        ),
    ]
