import scrapy
import time


class AnnouncementSpider(scrapy.Spider):
    def parse(self, response):
        print('parse called')

    name = "announcements"

    def start_requests(self):
        start_page_url_template = 'https://www.wg-gesucht.de/wg-zimmer-in-Darmstadt.23.0.1.<page_index>.html'

        for x in range(0, 30):
            url = start_page_url_template.replace('<page_index>', str(x))
            yield scrapy.Request(url=url, callback=self.parse_list_Page)

    def parse_list_Page(self, response):
        print('list page')
