#coding:utf-8
import codecs
import time
import sqlite3
import pymongo
import datetime
import redis
from pyecharts import Bar

class DataOutput(object):

    def __init__(self):
        self.datas=[]
        self.len=0
    def store_data(self,th,td):
        if th is None or td is None:
            return
        self.datas.append(th)
        self.datas.append(td)
        self.len=len(th)

    def output_html(self):
        s=str(time.time())
        fout=codecs.open('baike'+s+'.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body><center>")
        fout.write("<table>")
        for data in self.datas:
            count=self.len
            for l in data:
                if count==0:
                    count=self.len
                if count == self.len:
                    fout.write("<tr>")
                fout.write("<td>%s</td>"%l)
                count=count-1
                if count ==0:
                    fout.write("</tr>")
        fout.write("</table>")
        fout.write("</center></body>")
        fout.write("</html>")
        fout.close()

    def out_putchart(self):
        bar=Bar("船只进港情况")
        #bar.add("船只数量","shhd",23,render())

    def store_sqlite3(self,td):
        con=sqlite3.connect('chuanbo.db')
        cur=con.cursor()
        #cur.execute('CREATE TABLE chuanbo (id integer primary key,gangquname varchar(20),chuanname varchar(20),huhao varchar(10),MMSI integer,zhuangtai varchar(10),shijian varchar(25))')
        i=0
        for ts in td:
            gangqunname=td[i]
            chuanname=td[i+1]
            huhao=td[i+2]
            MMSI=td[i+3]
            zhuangtai=td[i+4]
            shijian=td[i+5]
            i=i+6
            cur.execute('INSERT INTO chuanbo VALUES (?,?,?,?,?,?)',gangqunname,chuanname,huhao,MMSI,zhuangtai,shijian)
        try:
            con.commit()
        except Exception:
            print "提交失败"
        con.close()


    def store_mongodb(self,td):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client.papers
        collection = db.chuanbo
        i=0
        for ts in td:
            chuan = {"gangqunname": td[i],
                    "chuanname": td[i+1],
                    "huhao": td[i+2],
                    "MMSI":td[i+3],
                    "zhuangtai":td[i+4],
                    "shijian":td[i+5],
                    "date": datetime.datetime.utcnow()
                    }
            chuan_id = collection.insert(chuan)
            i = i + 6
        collection.find_one({"gangqunname": "厦门"})
        for chuan in collection.find():
            print chuan
        for chuan in collection.find({"gangqunname": "厦门"}):
            print chuan
        client.close()

    def store_redis(self,td):
        r = redis.Redis(host='127.0.0.1', port=6379)
        r.set('name', 'qiye')
        i=0
        for ts in td:
            r.set("gangqunname", td[i])
            r.set("chuanname",td[i+1])
            r.set("huhao",td[i+2])
            r.set("MMSI",td[i+3])
            r.set("zhuangtai",td[i+4])
            r.set("shijian",td[i+5])
            i = i + 6
        print r.get('gangqunname')

