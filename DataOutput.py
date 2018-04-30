#coding:utf-8
import codecs
import time
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
