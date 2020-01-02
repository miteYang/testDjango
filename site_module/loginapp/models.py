
from django.db import models

# Create your models here.
class UserInfoManager(models.Manager):
    def all(self):
        return super().all().filter(sex='male')

class Group(models.Model):
    class Meta:
        verbose_name='用户组'
        verbose_name_plural='用户组'

    groupname=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.groupname


class User(models.Model):
    user1 = UserInfoManager()

    gender=(
        ('male','男'),
        ('female','女'),
    )
    id=models.CharField(primary_key=True,max_length=5,auto_created=True,default=1)
    name=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=200,unique=True,default='')
    sex=models.CharField(max_length=32,choices=gender,default='男')
    users=models.ForeignKey(Group,default='',verbose_name='用户组',on_delete=models.CASCADE)

    def __str__(self):
        return 'id='+self.id\
               +' | name='+self.name\
               +' | password='+self.password\
               +' | sex='+self.sex\
               +' | users='+self.users.__str__()

    class Meta:

        verbose_name='用户'
        verbose_name_plural='用户'

