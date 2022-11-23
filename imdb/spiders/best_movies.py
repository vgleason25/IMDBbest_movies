import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMovies2Spider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers={
            'User-Agent': self.user_agent
            })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1[@data-testid='hero-title-block__title']/text()").get(),
            'year': response.xpath("(//ul[@data-testid='hero-title-block__metadata']/li)[1]/span/text()").get(),
            'duration': response.xpath("normalize-space((//ul[@data-testid='hero-title-block__metadata']/li)[3])").get(),
            'genre': response.xpath("//div[@data-testid='genres']/div/a/span/text()").get(),
            'rating': response.xpath("(//ul[@data-testid='hero-title-block__metadata']/li)[2]/span/text()").get(),
            'imdb_rating': response.xpath("(//div[@data-testid='hero-rating-bar__aggregate-rating__score'])[2]/span[1]/text()").get(),
            'movie_url': response.url
        }
