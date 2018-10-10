import pymysql

class Sql:
    def __init__(self):
        self.db = pymysql.connect("localhost",'erp' ,'123456' ,"erpsql").cursor()
        
    def select(self,userName=None):
        self.db.execute('select * from user where name=%s ',userName)
        results = self.db.fetchall()
        return results

    def look(self,com=None):
        pass

    def up(self,dic):
        pass

    def dele(self,col):
        pass