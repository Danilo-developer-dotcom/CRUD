import sqlite3

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect("crud.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def execute(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.conn.commit()

    def select(self, query: str, fetch: int):
        self.cursor.execute(query)
        match fetch:
            case 1:
                return self.cursor.fetchall()
            case 2:
                return self.cursor.fetchone()

    def create_table(self):
        self.cursor.execute('''create table if not exists users (
                                    id integer primary key autoincrement,
                                    name text,
                                    profession text,
                                    payment real
                                    )''')


    def close(self):
        if self.conn:
            self.conn.close()
