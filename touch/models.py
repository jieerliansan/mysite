from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="名称");
    content = models.TextField(verbose_name="内容");
    date = models.DateTimeField(verbose_name="日期");

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章汇总'


class Product(models.Model):
    label = models.CharField(max_length=32, verbose_name="名称");
    article = models.ForeignKey(Article,verbose_name="文章");

    class Meta:
        verbose_name = '产品中心'
        verbose_name_plural = '产品中心'


class News(models.Model):
    label = models.CharField(max_length=32);
    article = models.ForeignKey(Article, verbose_name="文章");

    class Meta:
        verbose_name = '活动资讯'
        verbose_name_plural = '活动资讯'


class Team(models.Model):
    label = models.CharField(max_length=32);
    article = models.ForeignKey(Article, verbose_name="文章")

    class Meta:
        verbose_name = '专家团队'
        verbose_name_plural = '专家团队'


class Train(models.Model):
    label = models.CharField(max_length=32);
    article = models.ForeignKey(Article, verbose_name="文章")

    class Meta:
        verbose_name = '技术培训'
        verbose_name_plural = '技术培训'


class Question(models.Model):
    label = models.CharField(max_length=32);
    article = models.ForeignKey(Article, verbose_name="文章");

    class Meta:
        verbose_name = '常见问题'
        verbose_name_plural = '常见问题'


