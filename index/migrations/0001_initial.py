# Generated by Django 2.0.6 on 2018-07-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PK10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qishu', models.CharField(max_length=100, verbose_name='期数')),
                ('haoma', models.CharField(max_length=255, verbose_name='号码')),
                ('shijian', models.CharField(max_length=255, verbose_name='时间')),
            ],
        ),
    ]
