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
            'movie_url': response.url
        }

# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule


# class BestMoviesSpider(CrawlSpider):
#     name = 'best_movies'
#     allowed_domains = ['web.archive.org']
#     start_urls = ["http://web.archive.org/web/20220826105915/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating%20instead%20of%20https://www.imdb.com"]

#     rules = (
#         Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
#     )
# # #this gets both types of titles but only returns the titles...
# #     def parse_item(self, response):
# #         if "//div[@class='title_wrapper']/h1/text()":  
# #             yield {
# #                 'title' : response.xpath("//div[@class='title_wrapper']/h1/text()").get()
# #             }
# #         if "//h1[@data-testid='hero-title-block__title']/text()":
# #             yield {
# #                 'title' : response.xpath("//h1[@data-testid='hero-title-block__title']/text()").get(),
# #                 'year' : response.xpath("//ul[@data-testid='hero-title-block__metadata']/li[1]/span/text()").get(),
# #                 'duration': response.xpath("normalize-space(//ul[@data-testid='hero-title-block__metadata']/li[@role='presentation' and position() = 3])").get(),
# #                 'genre' : response.xpath("//a/span[@class='ipc-chip__text']/text()").getall(),
# #                 'rating' : response.xpath("//ul[@data-testid='hero-title-block__metadata']/li[2]/span/text()").get(),
# #                 'movie_url' : response.url
# #             }
#     def parse_item(self, response):
#         if response.xpath("//h1[@data-testid='hero-title-block__title']/text()").get() is not None:
#             yield {
#                 'title' : response.xpath("//h1[@data-testid='hero-title-block__title']/text()").get(),
#                 'year' : response.xpath("//ul[@data-testid='hero-title-block__metadata']/li[1]/span/text()").get(),
#                 'duration': response.xpath("normalize-space(//ul[@data-testid='hero-title-block__metadata']/li[@role='presentation' and position() = 3])").get(),
#                 'genre' : response.xpath("//a/span[@class='ipc-chip__text']/text()").getall(),
#                 'rating' : response.xpath("//ul[@data-testid='hero-title-block__metadata']/li[2]/span/text()").get(),
#                 'movie_url' : response.url
#             }
#         else:
#             pass
#         if response.xpath("//h1[@data-testid='hero-title-block__title']/text()").get() is None:
#             yield {
#                 'title' : response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
#                 'year' : response.xpath("//ul[@data-testid='hero-title-block__metadata']/li[1]/span/text()").get(),
#                 'duration': response.xpath("normalize-space(//ul[@data-testid='hero-title-block__metadata']/li[@role='presentation' and position() = 3])").get(),
#                 'genre' : response.xpath("//a/span[@class='ipc-chip__text']/text()").getall(),
#                 'rating' : response.xpath("//ul[@data-testid='hero-title-block__metadata']/li[2]/span/text()").get(),
#                 'movie_url' : response.url
#             }
#         else:
#             pass
#         # isExists = response.xpath("//h1[@data-testid='hero-title-block__title']/text()").get()
#         # if isExists != "None":
#         #     yield {
#         #         'title' : response.xpath("//div[@class='title_wrapper']/h1/text()").get()
#         #         #ill need some more stuff here but ill figure that out later
#         #     }
#         # else: 
#         #     pass
