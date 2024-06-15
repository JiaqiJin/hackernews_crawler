from scrapy.crawler import CrawlerProcess
import pandas as pd
import re
from database.hackernews_database import HackerNewsDatabase
from hackernews.spiders.hackernews_spider import HackernewsSpider

def word_count(title):
    words = re.findall(r'\b\w+(?:-\w+)*\b', title)
    return len(words)

class HackerNewsCrawler:
    def __init__(self):
        self.db = HackerNewsDatabase()

    def run_crawler(self):
        # Setup Scrapy crawler process
        process = CrawlerProcess(settings={
            'FEED_FORMAT': 'json',
            'FEED_URI': 'hackernews.json'
        })
        process.crawl(HackernewsSpider)
        process.start()

    def process_data(self):
        # Load scraped data into a DataFrame
        df = pd.read_json('hackernews.json')

        # Filter and sort entries
        df['title_word_count'] = df['title'].apply(word_count)
        more_than_five_words = df[df['title_word_count'] > 5].sort_values(by='comments', ascending=False)
        five_or_fewer_words = df[df['title_word_count'] <= 5].sort_values(by='points', ascending=False)

        return more_than_five_words, five_or_fewer_words

    def store_data(self, more_than_five_words, five_or_fewer_words):
        # Insert filtered data into database
        self.db.insert_entries(more_than_five_words, 'more_than_five_words')
        self.db.insert_entries(five_or_fewer_words, 'five_or_fewer_words')

    def close(self):
        self.db.close_connection()
        
        