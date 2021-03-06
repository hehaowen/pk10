# Generated by Django 2.0.6 on 2018-07-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Guan_Yada', models.FloatField(verbose_name='亚冠大')),
                ('Guan_Yaxiao', models.FloatField(verbose_name='亚冠大')),
                ('Guan_Yadan', models.FloatField(verbose_name='亚冠大')),
                ('Guan_Yashuang', models.FloatField(verbose_name='亚冠大')),
                ('Guan_da', models.FloatField(verbose_name='亚冠大')),
                ('Guan_xiao', models.FloatField(verbose_name='亚冠大')),
                ('Guan_dan', models.FloatField(verbose_name='亚冠大')),
                ('Guan_shuang', models.FloatField(verbose_name='亚冠大')),
                ('Guan_long', models.FloatField(verbose_name='亚冠大')),
                ('Guan_hu', models.FloatField(verbose_name='亚冠大')),
                ('ji_da', models.FloatField(verbose_name='亚冠大')),
                ('ji_xiao', models.FloatField(verbose_name='亚冠大')),
                ('ji_dan', models.FloatField(verbose_name='亚冠大')),
                ('ji_shuang', models.FloatField(verbose_name='亚冠大')),
                ('ji_long', models.FloatField(verbose_name='亚冠大')),
                ('ji_hu', models.FloatField(verbose_name='亚冠大')),
                ('san_da', models.FloatField(verbose_name='亚冠大')),
                ('san_xiao', models.FloatField(verbose_name='亚冠大')),
                ('san_dan', models.FloatField(verbose_name='亚冠大')),
                ('san_shuang', models.FloatField(verbose_name='亚冠大')),
                ('san_long', models.FloatField(verbose_name='亚冠大')),
                ('san_hu', models.FloatField(verbose_name='亚冠大')),
                ('si_da', models.FloatField(verbose_name='亚冠大')),
                ('si_xiao', models.FloatField(verbose_name='亚冠大')),
                ('si_dan', models.FloatField(verbose_name='亚冠大')),
                ('si_shuang', models.FloatField(verbose_name='亚冠大')),
                ('si_long', models.FloatField(verbose_name='亚冠大')),
                ('si_hu', models.FloatField(verbose_name='亚冠大')),
                ('wu_da', models.FloatField(verbose_name='亚冠大')),
                ('wu_xiao', models.FloatField(verbose_name='亚冠大')),
                ('wu_dan', models.FloatField(verbose_name='亚冠大')),
                ('wu_shuang', models.FloatField(verbose_name='亚冠大')),
                ('wu_long', models.FloatField(verbose_name='亚冠大')),
                ('wu_hu', models.FloatField(verbose_name='亚冠大')),
                ('liu_da', models.FloatField(verbose_name='亚冠大')),
                ('liu_xiao', models.FloatField(verbose_name='亚冠大')),
                ('liu_dan', models.FloatField(verbose_name='亚冠大')),
                ('liu_shuang', models.FloatField(verbose_name='亚冠大')),
                ('liu_long', models.FloatField(verbose_name='亚冠大')),
                ('liu_hu', models.FloatField(verbose_name='亚冠大')),
                ('qi_da', models.FloatField(verbose_name='亚冠大')),
                ('qi_xiao', models.FloatField(verbose_name='亚冠大')),
                ('qi_dan', models.FloatField(verbose_name='亚冠大')),
                ('qi_shuang', models.FloatField(verbose_name='亚冠大')),
                ('qi_long', models.FloatField(verbose_name='亚冠大')),
                ('qi_hu', models.FloatField(verbose_name='亚冠大')),
                ('ba_da', models.FloatField(verbose_name='亚冠大')),
                ('ba_xiao', models.FloatField(verbose_name='亚冠大')),
                ('ba_dan', models.FloatField(verbose_name='亚冠大')),
                ('ba_shuang', models.FloatField(verbose_name='亚冠大')),
                ('ba_long', models.FloatField(verbose_name='亚冠大')),
                ('ba_hu', models.FloatField(verbose_name='亚冠大')),
                ('jiu_da', models.FloatField(verbose_name='亚冠大')),
                ('jiu_xiao', models.FloatField(verbose_name='亚冠大')),
                ('jiu_dan', models.FloatField(verbose_name='亚冠大')),
                ('jiu_shuang', models.FloatField(verbose_name='亚冠大')),
                ('jiu_long', models.FloatField(verbose_name='亚冠大')),
                ('jiu_hu', models.FloatField(verbose_name='亚冠大')),
                ('shi_da', models.FloatField(verbose_name='亚冠大')),
                ('shi_xiao', models.FloatField(verbose_name='亚冠大')),
                ('shi_dan', models.FloatField(verbose_name='亚冠大')),
                ('shi_shuang', models.FloatField(verbose_name='亚冠大')),
                ('shi_long', models.FloatField(verbose_name='亚冠大')),
                ('shi_hu', models.FloatField(verbose_name='亚冠大')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
