# Hacker News Scraper

## Overview

This Python script scrapes the first 30 entries from Hacker News (https://news.ycombinator.com/), processes the data, and stores it in a SQLite database. It includes filtering based on title word count and sorting by points or comments.

### Prerequisites

- Python 3.x installed on your system
- `pip` package manager

## Installation

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### Clone Repository

```bash
git clone https://github.com/JiaqiJin/hackernews_crawler.git
cd hackernews
```

## Usage
### Running the Scraper

To run the Hacker News scraper, execute the following command in your terminal:

```bash
python main.py
```

## Workflow

1. Scraping: The script initiates a Scrapy crawler (HackernewsSpider) to fetch data from Hacker News.

2. Processing: Data is processed to calculate word count, filter entries based on title length, and sort entries by points or comments.

3. Database Storage: Filtered and sorted data (more_than_five_words and five_or_fewer_words) are stored in the SQLite database.

4. Execution: Run the script using Python : python main.py

5. Output: Scraper outputs are stored in hackernews.db and hackernews.json.

## How to run test

run command on your console
```bash
pytest
```