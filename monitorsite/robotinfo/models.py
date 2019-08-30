from django.db import models

# Create your models here.
class ytrbts(models.Model): #数据库新建ytrbts表，字段如下
    pos = models.CharField('位置',max_length=20)
    cart_pos = models.CharField('空间位置',max_length=150)
    jnt_pos = models.CharField('关节位置',max_length=50)
    jnt_vel = models.CharField('关节速度',max_length=50)
    jnt_trq = models.CharField('关节力矩',max_length=50)
    alarm_info = models.CharField('报警信息',max_length=10)
    state = models.CharField('机器人状态',max_length=10)
    running_state = models.CharField('是否运行',max_length=10)
