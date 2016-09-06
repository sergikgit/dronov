# -*- coding: windows-1251 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)

class Good(models.Model):
    name = models.CharField(max_length = 50, unique = True, db_index = True, verbose_name = "name")
    category = models.ForeignKey(Category, verbose_name = "categ")
    description = models.TextField(verbose_name = "descr")
    content = models.TextField(verbose_name = "cont")
    price = models.FloatField(db_index = True, verbose_name = "prc")
    price_acc = models.FloatField(null = True, blank = True, verbose_name = u"price22")
    in_stock = models.BooleanField(default = True, db_index = True, verbose_name = "instock")
    featured = models.BooleanField(default = False, db_index = True, verbose_name = "feat")
    #image = models.ImageField(upload_to = "goods/list", verbose_name = "Îñíîâíîå èçîáðàæåíèå")

    # def save(self, *args, **kwargs):
    #   try:
    #     this_record = Good.objects.get(pk = self.pk)
    #     if this_record.image != self.image:
    #       this_record.image.delete(save = False)
    #   except:
    #     pass
    #   super(Good, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #   self.image.delete(save = False)
    #   super(Good, self).delete(*args, **kwargs)

    # def get_absolute_url(self):
    #   return reverse("goods_detail", kwargs = {"pk": self.pk})

    class Meta:
        verbose_name = "verb"
        #verbose_name_plural = "plural"
