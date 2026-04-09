import sqlite3
from src.dbmanager import DbManager

class CRUD:
    def __init__(self):
        self.dbmanager = DbManager()

    def create(self, name: str, profession: str, payment: float):
        self.dbmanager.execute("insert into users (name, profession, payment) values (?, ?, ?)",
                               (name, profession, payment))
        return True

    def read(self):
        fetch = self.dbmanager.select("select * from users", 1)
        return fetch

    def update(self, row_id: int, column_name: str, new_value: str | float):
        self.dbmanager.execute(f'''update users
                                 set {column_name} = ?
                                 where id = ?''', (new_value, row_id))
        return True

    def delete(self, row_id: int):
        self.dbmanager.execute(f"delete from users where id = ?", (row_id,))
        return True
