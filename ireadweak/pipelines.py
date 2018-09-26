# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
# encoding: utf-8

import sys
sys.path.append('/Users/laojiaqi/openProject/pan-baidu-download')

import bddown_cli

import  MySQLdb


# write file
class IreadweakPipeline(object):

    num=0

    def open_spider(self, spider):
        self.file = codecs.open('files2.txt', 'wb+', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write("%-5s %-5s,%-10s,%-10s \n"% (self.num,item['title'],item['author'],item['download_link']))
        self.num+=1
        self.file.write("\n")
        bddown_cli.execute_command(['download',item['download_link']])
        return item

    def spider_closed(self, spider):
        self.file.close()



# insert into DateBase
class DateBasePipeline(object):
    insert_sql = "insert into book (description,download_link,category,title,author) values(%s,%s,%s,%s,%s)"

    def open_spider(self, spider):
        self.db = MySQLdb.connect("localhost", "root", "password", "yishu", charset='utf8')
        self.cursor = self.db.cursor()
        self.count = 0

    def process_item(self, item, spider):

        try:
            self.cursor.execute(self.insert_sql,(item['description'],item['download_link'],item['category'],item['title'],item['author']))
            self.db.commit()
            self.count += 1
        except BaseException,aru:
            print"insert fail %s" % aru
        return item

    def spider_closed(self, spider):
        self.db.close()
        pass