# Generated by Django 2.0.6 on 2018-07-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_odds_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='odds',
            name='ba_hu',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='ba_long',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='jiu_hu',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='jiu_long',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='liu_hu',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='liu_long',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='qi_hu',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='qi_long',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='shi_hu',
        ),
        migrations.RemoveField(
            model_name='odds',
            name='shi_long',
        ),
        migrations.AddField(
            model_name='odds',
            name='ya_da',
            field=models.FloatField(default='1.982', verbose_name='亚大'),
        ),
        migrations.AddField(
            model_name='odds',
            name='ya_dan',
            field=models.FloatField(default='1.982', verbose_name='亚单'),
        ),
        migrations.AddField(
            model_name='odds',
            name='ya_hu',
            field=models.FloatField(default='1.982', verbose_name='亚虎'),
        ),
        migrations.AddField(
            model_name='odds',
            name='ya_long',
            field=models.FloatField(default='1.982', verbose_name='亚龙'),
        ),
        migrations.AddField(
            model_name='odds',
            name='ya_shuang',
            field=models.FloatField(default='1.982', verbose_name='亚双'),
        ),
        migrations.AddField(
            model_name='odds',
            name='ya_xiao',
            field=models.FloatField(default='1.982', verbose_name='亚小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_Yada',
            field=models.FloatField(default='1.982', verbose_name='亚冠大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_Yadan',
            field=models.FloatField(default='1.982', verbose_name='亚冠单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_Yashuang',
            field=models.FloatField(default='1.982', verbose_name='亚冠双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_Yaxiao',
            field=models.FloatField(default='1.982', verbose_name='亚冠小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_da',
            field=models.FloatField(default='1.982', verbose_name='冠大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_dan',
            field=models.FloatField(default='1.982', verbose_name='冠单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_hu',
            field=models.FloatField(default='1.982', verbose_name='冠虎'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_long',
            field=models.FloatField(default='1.982', verbose_name='冠龙'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_shuang',
            field=models.FloatField(default='1.982', verbose_name='冠双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='Guan_xiao',
            field=models.FloatField(default='1.982', verbose_name='冠小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ba_da',
            field=models.FloatField(default='1.982', verbose_name='八大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ba_dan',
            field=models.FloatField(default='1.982', verbose_name='八单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ba_shuang',
            field=models.FloatField(default='1.982', verbose_name='八双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ba_xiao',
            field=models.FloatField(default='1.982', verbose_name='八小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ji_da',
            field=models.FloatField(default='1.982', verbose_name='季大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ji_dan',
            field=models.FloatField(default='1.982', verbose_name='季单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ji_hu',
            field=models.FloatField(default='1.982', verbose_name='季虎'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ji_long',
            field=models.FloatField(default='1.982', verbose_name='季龙'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ji_shuang',
            field=models.FloatField(default='1.982', verbose_name='季双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='ji_xiao',
            field=models.FloatField(default='1.982', verbose_name='季小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='jiu_da',
            field=models.FloatField(default='1.982', verbose_name='九大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='jiu_dan',
            field=models.FloatField(default='1.982', verbose_name='九单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='jiu_shuang',
            field=models.FloatField(default='1.982', verbose_name='九双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='jiu_xiao',
            field=models.FloatField(default='1.982', verbose_name='九小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='liu_da',
            field=models.FloatField(default='1.982', verbose_name='六大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='liu_dan',
            field=models.FloatField(default='1.982', verbose_name='六单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='liu_shuang',
            field=models.FloatField(default='1.982', verbose_name='六双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='liu_xiao',
            field=models.FloatField(default='1.982', verbose_name='六小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='qi_da',
            field=models.FloatField(default='1.982', verbose_name='七大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='qi_dan',
            field=models.FloatField(default='1.982', verbose_name='七单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='qi_shuang',
            field=models.FloatField(default='1.982', verbose_name='七双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='qi_xiao',
            field=models.FloatField(default='1.982', verbose_name='七小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='san_da',
            field=models.FloatField(default='1.982', verbose_name='三大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='san_dan',
            field=models.FloatField(default='1.982', verbose_name='三单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='san_hu',
            field=models.FloatField(default='1.982', verbose_name='三虎'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='san_long',
            field=models.FloatField(default='1.982', verbose_name='三龙'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='san_shuang',
            field=models.FloatField(default='1.982', verbose_name='三双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='san_xiao',
            field=models.FloatField(default='1.982', verbose_name='三小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='shi_da',
            field=models.FloatField(default='1.982', verbose_name='十大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='shi_dan',
            field=models.FloatField(default='1.982', verbose_name='十单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='shi_shuang',
            field=models.FloatField(default='1.982', verbose_name='十双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='shi_xiao',
            field=models.FloatField(default='1.982', verbose_name='十小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='si_da',
            field=models.FloatField(default='1.982', verbose_name='四大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='si_dan',
            field=models.FloatField(default='1.982', verbose_name='四单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='si_hu',
            field=models.FloatField(default='1.982', verbose_name='四虎'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='si_long',
            field=models.FloatField(default='1.982', verbose_name='四龙'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='si_shuang',
            field=models.FloatField(default='1.982', verbose_name='四双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='si_xiao',
            field=models.FloatField(default='1.982', verbose_name='四小'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='wu_da',
            field=models.FloatField(default='1.982', verbose_name='五大'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='wu_dan',
            field=models.FloatField(default='1.982', verbose_name='五单'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='wu_hu',
            field=models.FloatField(default='1.982', verbose_name='五虎'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='wu_long',
            field=models.FloatField(default='1.982', verbose_name='五龙'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='wu_shuang',
            field=models.FloatField(default='1.982', verbose_name='五双'),
        ),
        migrations.AlterField(
            model_name='odds',
            name='wu_xiao',
            field=models.FloatField(default='1.982', verbose_name='五小'),
        ),
    ]
