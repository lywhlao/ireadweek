# encoding: utf-8
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ireadweak.items import IreadweakItem


class IReadSpider(CrawlSpider):
    name = "IReadSpider"
    allowed_domains = ['ireadweek.com']
    start_urls = ['http://www.ireadweek.com/index.php']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('/bookInfo/\d+\.html', )),callback='parse_content'),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('/index/\d+\.html', )),follow=True),
    )

    def encode_item(self, item):
        if item['title']:
            item['title'] = item['title'].encode('utf-8')
        if item['author']:
            item['author'] = item['author'].encode('utf-8')
        if item['category']:
            item['category'] = item['category'].encode('utf-8')
        if item['download_link']:
            item['download_link'] = item['download_link'].encode('utf-8')
        if item['desc']:
            item['desc'] = item['desc'].encode('utf-8')

    def parse_content(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item=IreadweakItem()
        item['title']=response.css('div[class=hanghang-za-title]:nth-child(1)::text').extract_first()
        item['author']=response.css('div[class=hanghang-shu-content-font]>p:nth-child(1)::text').extract_first()
        item['category']=response.css('div[class=hanghang-shu-content-font]>p:nth-child(2)::text').extract_first()
        item['download_link']=response.css('div[class=hanghang-shu-content-btn]>a::attr(href)').extract_first()
        item['desc']=response.css('div[class=hanghang-shu-content-font]>p:nth-child(6)::text').extract_first()
        # self.encode_item(item)
        return item
