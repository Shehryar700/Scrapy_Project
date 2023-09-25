import scrapy
from quotes.items import AboutItem

class DetailedPage(scrapy.Spider):
    name = "detailed"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for about_link in response.css('a[href^="/author/"]::attr(href)').getall():
            yield response.follow(about_link, callback=self.parse_about_page)
            # Follow pagination links
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    def parse_about_page(self, response):
        # Parse data from the "about" page
        item = AboutItem()
        item['name'] = response.css('h3.author-title::text').get()
        item['birthdate'] = response.css('span.author-born-date::text').get()
        item['location'] = response.css('span.author-born-location::text').get()
        item['description'] = response.css('div.author-description::text').get().strip()
        yield item
