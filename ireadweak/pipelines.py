# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
# encoding: utf-8

class IreadweakPipeline(object):

    num=0

    def open_spider(self, spider):
        self.file = codecs.open('files.txt', 'wb+', encoding='utf-8')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False, sort_keys=True) + "\n"
        # self.file.write("<tr>")
        # self.file.write(" %s</td>" % ''.join(item['title']))
        # self.file.write("<td> %s</td>" % ''.join(item['author']))
        # self.file.write("<td><a href=%s> %s</td>" % (''.join(item['download_link']), ''.join(item['download_link'])))
        # self.file.write("<td> %s</td>" % ''.join(item['desc']))
        # self.file.write("</tr>")
        self.file.write("%-5s %-5s,%-10s,%-10s \n"% (self.num,item['title'],item['author'],item['download_link']))
        # self.file.write("       "+item['author'])
        # self.file.write("       "+item['desc'])
        self.num+=1
        self.file.write("\n")
        return item


    def spider_closed(self, spider):
        self.file.close()


    # def __init__(self):
    #     self.file = codecs.open('list.html', 'wb+', encoding='utf-8')
    #     self.file.write("<html>")
    #     self.file.write("<body>")
    #     self.file.write("<table>")
    #
    # def process_item(self, item, spider):
    #     # line = json.dumps(dict(item), ensure_ascii=False, sort_keys=True) + "\n"
    #     self.file.write("<tr>")
    #     self.file.write("<td> %s</td>" % ''.join(item['title']))
    #     self.file.write("<td> %s</td>" % ''.join(item['author']))
    #     self.file.write("<td><a href=%s> %s</td>" % (''.join(item['download_link']), ''.join(item['download_link'])))
    #     self.file.write("<td> %s</td>" % ''.join(item['desc']))
    #     self.file.write("</tr>")
    #     return item

    # def spider_closed(self, spider):
    #     self.file.write("</table>")
    #     self.file.write("</body>")
    #     self.file.write("</html>")
    #     self.file.close()