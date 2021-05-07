import scrapy


class GetPopularCategoriesSpider(scrapy.Spider):
    name = "get_popular_categories"
    
    start_urls = [
        'https://www.aliexpress.com/popular.html'
    ]

    def parse(self, response):
        categories = response.css('div.channel-content')
        yield{
            'title': categories.css('a.title::text').getall()
        }