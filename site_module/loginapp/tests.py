import pymysql
from django.test import TestCase

# Create your tests here.
from django.db import models


class User():
    # user1 = UserInfoManager()

    gender=(
        ('male','男'),
        ('female','女'),
    )
    id=''
    name=''
    password=''
    sex=''
    # users=0

    def __str__(self):
        return 'id='+self.id\
               +' | name='+self.name\
               +' | password='+self.password\
               +' | sex='+self.sex


def test_sql_con(self):
    db = pymysql.connect('rm-wz9eorq112a17vk3huo.mysql.rds.aliyuncs.com', 'yzj000', 'yzj123000!', 'mite_obj')
    cur = db.cursor()
    sql_t = 'SELECT * FROM loginapp_user ;'
    # 2019-05-28 10:08:10开始
    try:
        cur.execute(sql_t)
        result = cur.fetchall()
        # print(result)
        List1 = []
        for i in result:
            # print(i, type(i))
            user=User()
            user.id=i[0]
            user.name=i[1]
            user.password=i[2]
            user.sex=i[3]

            List1.append(user)
        # print(List1, len(List1))
        return List1
    except BaseException as b1:
        print('error', b1)
    db.close()

test_sql_con(None)