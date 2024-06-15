import sqlite3

class SQLitePipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect("hackernews.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER,
                title TEXT,
                points INTEGER,
                comments INTEGER,
                request_timestamp TEXT,
                applied_filter TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO entries (number, title, points, comments, request_timestamp, applied_filter)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item['number'],
            item['title'],
            item['points'],
            item['comments'],
            item['request_timestamp'],
            item['applied_filter']
        ))
        self.connection.commit()
        return item
