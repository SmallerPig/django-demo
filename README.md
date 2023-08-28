## what's this?

这是一个演示Django项目后台使用二级联动效果的demo

## how to use it?

- download或者clone项目到本地目录
- cd到项目目录
- 生成数据库文件
```
$python manage.py makemigrations linkage
$python manage.py migrate
```
- 创建超级管理员
```
$python manage.py createsuperuser
Username (leave blank to use 'smallerpig'):
Email address: zhuqiwuxi#gmail.com
Password:
Password (again):
Superuser created successfully.
edit some
```

- 启动本地调试服务器
```
$python manage.py runserver
```

- 使用刚才创建的超级管理员进入后台并先后创建省份、城市

- 最后在创建address就可以看到二级联动的效果了。

**Note:**需要手动添加省市数据

## 项目说明地址：
http://blog.smallerpig.com/1125.html
