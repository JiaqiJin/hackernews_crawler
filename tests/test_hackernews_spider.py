import pytest
import json
from scrapy.http import HtmlResponse
from scrapy.utils.test import get_crawler
from hackernews.spiders.hackernews_spider import HackernewsSpider


def test_filter_more_than_five_words():
    spider = HackernewsSpider()
    items = [
        {'number': '1.', 'title': 'This is a long title with more than five words', 'points': 10, 'comments': 5},
        {'number': '2.', 'title': 'Short title', 'points': 8, 'comments': 3},
        {'number': '3.', 'title': 'Another long title with many words', 'points': 12, 'comments': 8}
    ]

    filtered_items = spider.filter_more_than_five_words(items)
    
    assert len(filtered_items) == 2
    assert filtered_items[0]['title'] == 'Another long title with many words'
    assert filtered_items[1]['title'] == 'This is a long title with more than five words'

def test_filter_five_or_fewer_words():
    spider = HackernewsSpider()
    items = [
        {'number': '1.', 'title': 'This is short', 'points': 10, 'comments': 5},
        {'number': '2.', 'title': 'A very brief', 'points': 8, 'comments': 3},
        {'number': '3.', 'title': 'Short title', 'points': 12, 'comments': 8}
    ]

    filtered_items = spider.filter_five_or_fewer_words(items)
    
    assert len(filtered_items) == 3
    assert filtered_items[0]['title'] == 'Short title'
    assert filtered_items[1]['title'] == 'This is short'
