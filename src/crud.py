import sqlite3

class CRUD:
    def __init__(self):
        self.conn = sqlite3.connect('crud.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''create table if not exists users (
                                    id integer primary key autoincrement,
                                    name text,
                                    profession text,
                                    payment real
                                    )''')

    def create(self, name: str, profession: str, payment: float):
        self.cursor.execute('insert into users (name, profession, payment) values (?, ?, ?)', (name, profession, payment))
        self.conn.commit()
        print('[OK] - Values entered successfully')

    def read(self):
        self.cursor.execute("select * from users")
        return self.cursor.fetchall()

    def update(self, row_id: int, column_name: str, new_value: str | float):
        self.cursor.execute(f'''update users
                                set {column_name} = ?
                                where id = ?''', (new_value, row_id))
        self.conn.commit()
        print('[OK] - Values updated')

    def delete(self, row_id: int):
        self.cursor.execute(f"delete from users where id = ?",  (row_id,))
        self.conn.commit()
        print(f'[OK] - Row {row_id} deleted')

    def is_content(self):
        self.cursor.execute("select * from users limit 1;")
        result = self.cursor.fetchone()
        return result

    def close(self):
        if self.conn:
            self.conn.close()
