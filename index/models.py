from django.db import models


# Create your models here.
class PK10(models.Model):
    qishu = models.CharField(max_length=100, verbose_name='期数')
    haoma = models.CharField(max_length=255, verbose_name='号码')
    shijian = models.CharField(max_length=255, verbose_name='时间')

    def __str__(self):
        return self.qishu

    class Meta:
        pass


class Odds(models.Model):
    Guan_Yada = models.FloatField(verbose_name='亚冠大',default='1.982')
    Guan_Yaxiao = models.FloatField(verbose_name='亚冠小',default='1.982')
    Guan_Yadan = models.FloatField(verbose_name='亚冠单',default='1.982')
    Guan_Yashuang = models.FloatField(verbose_name='亚冠双',default='1.982')
    Guan_da = models.FloatField(verbose_name='冠大',default='1.982')
    Guan_xiao = models.FloatField(verbose_name='冠小',default='1.982')
    Guan_dan = models.FloatField(verbose_name='冠单',default='1.982')
    Guan_shuang = models.FloatField(verbose_name='冠双',default='1.982')
    Guan_long = models.FloatField(verbose_name='冠龙',default='1.982')
    Guan_hu = models.FloatField(verbose_name='冠虎',default='1.982')
    ya_da = models.FloatField(verbose_name='亚大',default='1.982')
    ya_xiao = models.FloatField(verbose_name='亚小',default='1.982')
    ya_dan = models.FloatField(verbose_name='亚单',default='1.982')
    ya_shuang = models.FloatField(verbose_name='亚双',default='1.982')
    ya_long = models.FloatField(verbose_name='亚龙',default='1.982')
    ya_hu = models.FloatField(verbose_name='亚虎',default='1.982')
    ji_da = models.FloatField(verbose_name='季大',default='1.982')
    ji_xiao = models.FloatField(verbose_name='季小',default='1.982')
    ji_dan = models.FloatField(verbose_name='季单',default='1.982')
    ji_shuang = models.FloatField(verbose_name='季双',default='1.982')
    ji_long = models.FloatField(verbose_name='季龙',default='1.982')
    ji_hu = models.FloatField(verbose_name='季虎',default='1.982')
    san_da = models.FloatField(verbose_name='三大',default='1.982')
    san_xiao = models.FloatField(verbose_name='三小',default='1.982')
    san_dan = models.FloatField(verbose_name='三单',default='1.982')
    san_shuang = models.FloatField(verbose_name='三双',default='1.982')
    san_long = models.FloatField(verbose_name='三龙',default='1.982')
    san_hu = models.FloatField(verbose_name='三虎',default='1.982')
    si_da = models.FloatField(verbose_name='四大',default='1.982')
    si_xiao = models.FloatField(verbose_name='四小',default='1.982')
    si_dan = models.FloatField(verbose_name='四单',default='1.982')
    si_shuang = models.FloatField(verbose_name='四双',default='1.982')
    si_long = models.FloatField(verbose_name='四龙',default='1.982')
    si_hu = models.FloatField(verbose_name='四虎',default='1.982')
    wu_da = models.FloatField(verbose_name='五大',default='1.982')
    wu_xiao = models.FloatField(verbose_name='五小',default='1.982')
    wu_dan = models.FloatField(verbose_name='五单',default='1.982')
    wu_shuang = models.FloatField(verbose_name='五双',default='1.982')
    wu_long = models.FloatField(verbose_name='五龙',default='1.982')
    wu_hu = models.FloatField(verbose_name='五虎',default='1.982')
    liu_da = models.FloatField(verbose_name='六大',default='1.982')
    liu_xiao = models.FloatField(verbose_name='六小',default='1.982')
    liu_dan = models.FloatField(verbose_name='六单',default='1.982')
    liu_shuang = models.FloatField(verbose_name='六双',default='1.982')
    qi_da = models.FloatField(verbose_name='七大',default='1.982')
    qi_xiao = models.FloatField(verbose_name='七小',default='1.982')
    qi_dan = models.FloatField(verbose_name='七单',default='1.982')
    qi_shuang = models.FloatField(verbose_name='七双',default='1.982')
    ba_da = models.FloatField(verbose_name='八大',default='1.982')
    ba_xiao = models.FloatField(verbose_name='八小',default='1.982')
    ba_dan = models.FloatField(verbose_name='八单',default='1.982')
    ba_shuang = models.FloatField(verbose_name='八双',default='1.982')
    jiu_da = models.FloatField(verbose_name='九大',default='1.982')
    jiu_xiao = models.FloatField(verbose_name='九小',default='1.982')
    jiu_dan = models.FloatField(verbose_name='九单',default='1.982')
    jiu_shuang = models.FloatField(verbose_name='九双',default='1.982')
    shi_da = models.FloatField(verbose_name='十大',default='1.982')
    shi_xiao = models.FloatField(verbose_name='十小',default='1.982')
    shi_dan = models.FloatField(verbose_name='十单',default='1.982')
    shi_shuang = models.FloatField(verbose_name='十双',default='1.982')

    def __str__(self):
        return self.Guan_Yada


class User(models.Model):
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account
