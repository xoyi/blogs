from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=30, verbose_name='标题')
    creat_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hcontent = models.TextField(max_length=1000)
    is_deleted = models.BooleanField()
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.hname