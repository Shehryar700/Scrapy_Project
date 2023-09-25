import scrapy
from quotes.items import QuotesItem

class MySpider(scrapy.Spider):
    name = "xbot"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # Scrape quotes on the current page
        quotes_list = response.css('div.quote')
        for quote in quotes_list:
            item = QuotesItem()
            item['quote'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('a.tag::text').getall()

            # Convert the list of tags into a comma-separated string
            item['tags'] = ', '.join(item['tags'])
            yield item

        # Follow the "Next" button
        next_page = response.css('li.next > a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
