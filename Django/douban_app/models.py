# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#数据库模型 可以直接由数据库的表生成  python manage.py inspectdb> douban_app/models
class Douban(models.Model):
    title = models.CharField(max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    star = models.CharField(max_length=255, blank=True, null=True)
    quote = models.CharField(max_length=255, blank=True, null=True)
    img_src = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban'

"""
class Douban2(models.Model):
    title = models.CharField(max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    star = models.CharField(max_length=255, blank=True, null=True)
    quote = models.CharField(max_length=255, blank=True, null=True)
    img_src = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban2'
"""