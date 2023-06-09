# Generated by Django 4.2.1 on 2023-05-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StateStats',
            fields=[
                ('state_code', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='State Code')),
                ('state_name', models.CharField(max_length=45, verbose_name='State Name')),
                ('rigid', models.FloatField(default=0, verbose_name='Rigid')),
                ('flexible', models.FloatField(default=0, verbose_name='Flexible')),
                ('mlp', models.FloatField(default=0, verbose_name='MLP')),
            ],
            options={
                'db_table': 'state_statistics',
            },
        ),
    ]
