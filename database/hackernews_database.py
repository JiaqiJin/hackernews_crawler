import sqlite3
import datetime
import pandas as pd

class HackerNewsDatabase:
    def __init__(self, db_name='hackernews.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER,
                title TEXT,
                points INTEGER,
                comments INTEGER,
                request_timestamp TEXT,
                applied_filter TEXT,
                title_word_count INTEGER 
            )
        ''')
        self.connection.commit()

    def insert_entries(self, df, applied_filter):
        current_time = datetime.datetime.now().isoformat()
        df['request_timestamp'] = current_time
        df['applied_filter'] = applied_filter
        df.to_sql('entries', self.connection, if_exists='append', index=False)

    def close_connection(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

