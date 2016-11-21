# !/usr/bin/env python
# -*- coding:utf-8 -*-
# _ _author__ = 'cmcc.smp'

import json
from django.shortcuts import render, HttpResponse
from .models import City
# Create your views here.


def get_city(request, provience_id):
    # 根据传递的省的id 查找数据库中该省的城市
    citys = City.objects.filter(provience_id=provience_id)
    result = []
    for i in citys:
        # 对应的id和城市名称组成一个字典
        result.append({'id':i.id, 'name':i.name})
    # 返回json数据
    return HttpResponse(json.dumps(result), content_type="application/json")