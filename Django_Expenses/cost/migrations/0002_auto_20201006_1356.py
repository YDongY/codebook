# Generated by Django 3.1.2 on 2020-10-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '消费类型', 'verbose_name_plural': '消费类型'},
        ),
    ]