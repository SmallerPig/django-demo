# !/usr/bin/env python
# -*- coding:utf-8 -*-
# _ _author__ = 'cmcc.smp'
from django.contrib import admin
from .models import Provience, City, Add_ress
# Register your models here.

admin.site.register(Provience)
admin.site.register(City)
admin.site.register(Add_ress)
