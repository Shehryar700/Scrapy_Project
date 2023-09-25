import scrapy
from quotes.items import CombinedItem

class CombinedSpider(scrapy.Spider):
    name = "combination"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = CombinedItem()
            item['quote'] = quote.css('span.text::text').get()
            item['tags'] = quote.css('a.tag::text').getall()
            item['tags'] = ', '.join(item['tags'])

            author_link = quote.css('small.author ~ a::attr(href)').get()
            if author_link:
                yield response.follow(author_link, callback=self.parse_author, meta={'quote_item': item})
            else:
                # If there are no author details link, yield the quote item directly
                yield item

        # Follow the "Next" button
        next_page = response.css('li.next > a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        author_item = CombinedItem()
        author_item['name'] = response.css('h3.author-title::text').get()
        author_item['birthdate'] = response.css('span.author-born-date::text').get()
        author_item['location'] = response.css('span.author-born-location::text').get()
        author_item['description'] = response.css('div.author-description::text').get().strip()

        quote_item = response.meta['quote_item']
        author_item['quote'] = quote_item['quote']
        author_item['tags'] = quote_item['tags']

        yield author_item
