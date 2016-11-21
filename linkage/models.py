# !/usr/bin/env python
# -*- coding:utf-8 -*-
# _ _author__ = 'cmcc.smp'

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Provience(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name



class City(models.Model):
	name = models.CharField(max_length=200)
	provience = models.ForeignKey('Provience', models.DO_NOTHING, db_column='provience_id')

	def __str__(self):
		return self.name


class Add_ress(models.Model):
	name = models.CharField(max_length=200)
	provience = models.ForeignKey('Provience', models.DO_NOTHING, db_column='provience_id')
	city = models.ForeignKey('City', models.DO_NOTHING, db_column='city_id')

	def __str__(self):
		return self.name
