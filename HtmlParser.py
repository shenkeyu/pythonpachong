#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup
import lxml


class HtmlParser(object):

    def parser(self,page_url,htmlcont,label,text,prettifylabel):
        if label is None or htmlcont is None or text is None or page_url is None or prettifylabel is None:
            return
        soup = BeautifulSoup(htmlcont,'lxml')
        new_url=self._get_new_urls(page_url,soup)
        new_th= self._get_new_thelements(page_url,soup,label,text)
        new_td= self._get_new_tdelements(page_url,soup,label,text,prettifylabel)
        return new_th,new_td,new_url



    def _get_new_thelements(self,page_url,soup,label,text1):
        new_th =[]
        p=soup.find(label,text=text1)
        if p is not None:
            pp=p.parent.parent
            for child1 in pp.find_all(label):
                    if child1 is not None:
                        new_th.append(child1.string)
                    else:
                        new_th.append("空")
        else:
            new_th="meiyou"
        return  new_th

    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup:soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标签
        #原书代码
        # links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        #2017-07-03 更新,原因百度词条的链接形式发生改变
        links = soup.find_all('a', href=re.compile(r'http://www.chinaports.com/'))
        if links is not None:
            for link in links:
                #提取href属性
                new_url = link['href']
                #拼接成完整网址
                #new_full_url = urlparse.urljoin(page_url,new_url)
                new_urls.add(new_url)
        else:
            new_urls="meiyou"
        return new_urls


    def _get_new_tdelements(self,page_url,soup,label,text1,childlabel):
        data=[]
        child=soup.find(label,text=text1)
        if child is not None:
            pp=child.parent.parent
            for child1 in pp.find_all(childlabel):
                    if child1 is not None:
                         data.append(child1.string)
                    else:
                            data.append("空")
        else:
            data="meiyou"
        return data
