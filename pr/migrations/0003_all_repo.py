# Generated by Django 4.1.5 on 2023-03-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0002_rtosapps_delete_rtosapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALL_Repo',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False, verbose_name='hmicsandbox_index')),
                ('Developer_Email_ID', models.EmailField(max_length=254, verbose_name='hmicsandbox_email')),
                ('Repo', models.CharField(max_length=20, verbose_name='hmicsandbox_Repo')),
                ('Last_Merge_Branch', models.CharField(max_length=20, verbose_name='hmicsandbox_merge_branch')),
                ('Open_PR', models.IntegerField(verbose_name='hmicsandbox_open_pr')),
                ('Merged_PR', models.IntegerField(verbose_name='hmicsandbox_close_pr')),
                ('Declined_PR', models.IntegerField(verbose_name='hmicsandbox_decline_pr')),
                ('Open_PR_DateTime', models.TextField(verbose_name='hmicsandbox open date time')),
                ('Close_PR_DateTime', models.TextField(verbose_name='hmicsandbox close date time')),
                ('Declined_PR_DateTime', models.TextField(verbose_name='hmicsandbox decline date time')),
                ('Ages_of_Open_PR', models.TextField()),
                ('Ages_of_Close_PR', models.TextField()),
            ],
        ),
    ]
