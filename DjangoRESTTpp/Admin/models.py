from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.



class AdminUser(models.Model):
    a_username = models.CharField(max_length=16,unique=True)#用户名
    a_password =models.CharField(max_length=256)#密码

    is_delete = models.BooleanField(default=False)#是否删除
    is_super = models.BooleanField(default=False)#是否

    #进行加密
    def set_password(self,password):
        self.a_password = make_password(password)
    def check_admin_password(self,password):
        return check_password(password,self.a_password)