from hackernews_crawler import HackerNewsCrawler

def main():
    
    crawler = HackerNewsCrawler()
    crawler.run_crawler()

    more_than_five_words, five_or_fewer_words = crawler.process_data()
    crawler.store_data(more_than_five_words, five_or_fewer_words)

    crawler.close()
    
    print("Entries with more than five words in the title (sorted by comments):")
    print(more_than_five_words)

    print("\nEntries with five or fewer words in the title (sorted by points):")
    print(five_or_fewer_words)
    
if __name__ == "__main__":
    main()