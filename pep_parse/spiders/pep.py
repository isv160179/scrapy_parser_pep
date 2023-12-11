import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_NUMBER_NAME, ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [f'https://{ALLOWED_DOMAINS}/']

    def parse(self, response):
        pep_list = response.css('section#numerical-index a::attr(href)')

        for pep in pep_list:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title_pep = response.css('h1.page-title::text').get()
        number, name = re.search(PEP_NUMBER_NAME, title_pep).groups()
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
