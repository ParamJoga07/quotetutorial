import scrapy
from ..items import QuotetutorialItem


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes'
    page_no = int(input("enter the pages you want to scrap:"))
    print()
    i = 1
    while i <= page_no:
        start_urls = ['https://quotes.toscrape.com/page/' + str(i)]

        def parse(self, response):
            items = QuotetutorialItem()
            all_div_quotes = response.css("div.quote")

            for quotes in all_div_quotes:
                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tags = quotes.css('.tag::text').extract()

                items['title'] = title
                items['author'] = author
                items['tags'] = tags

                yield items

        i = i + 1


if __name__ == '__main__':
    parse(self, response)
