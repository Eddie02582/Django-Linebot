# Generated by Django 3.2 on 2021-04-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packageId', models.PositiveIntegerField()),
                ('stickerId', models.PositiveIntegerField()),
                ('keyword', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
