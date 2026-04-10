import sqlite3

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect("crud.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def update(self, column_name, parameters):
        self.cursor.execute(f'''update users
                                 set {column_name} = ?
                                 where id = ?''', parameters)
        self.conn.commit()
        return self.cursor.rowcount


    def delete(self, row_id):
        self.cursor.execute(f"delete from users where id = ?", (row_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def insert(self, parameters):
        self.cursor.execute("insert into users (name, profession, payment) values (?, ?, ?)",
                            parameters)
        self.conn.commit()

    def select_all(self):
        self.cursor.execute("select * from users")
        return self.cursor.fetchall()

    def select_one(self):
        self.cursor.execute("select * from users limit 1;")
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
