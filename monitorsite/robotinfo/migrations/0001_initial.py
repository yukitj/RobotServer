# Generated by Django 2.2.2 on 2019-08-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ytrbts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=20, verbose_name='位置')),
                ('cart_pos', models.CharField(max_length=150, verbose_name='空间位置')),
                ('jnt_pos', models.CharField(max_length=50, verbose_name='关节位置')),
                ('jnt_vel', models.CharField(max_length=50, verbose_name='关节速度')),
                ('jnt_trq', models.CharField(max_length=50, verbose_name='关节力矩')),
                ('alarm_info', models.CharField(max_length=10, verbose_name='报警信息')),
                ('state', models.CharField(max_length=10, verbose_name='机器人状态')),
                ('running_state', models.CharField(max_length=10, verbose_name='是否运行')),
            ],
        ),
    ]
