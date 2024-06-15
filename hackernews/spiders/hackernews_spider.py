import scrapy
from hackernews.items import HackernewsItem
import datetime

class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        for index, item in enumerate(response.css('tr.athing')[:30], start=1):
            title = item.css('.titleline a::text').get()
            subtext = item.xpath('following-sibling::tr[1]').css('.subtext')
            points = subtext.css('.score::text').get()
            comments = subtext.css('a::text')[-1].get()
            points = int(points.split()[0]) if points else 0
            comments = int(comments.split()[0]) if comments and comments.split()[0].isdigit() else 0

            request_timestamp = datetime.datetime.now().isoformat()

            yield HackernewsItem(
                number=index,
                title=title,
                points=points,
                comments=comments,
                request_timestamp=request_timestamp,
                applied_filter=None  # Initially, no filter applied
            )