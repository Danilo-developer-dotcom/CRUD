from src.dbmanager import DbManager


class CRUD:
    def __init__(self, dbmanager: DbManager):
        self.dbmanager = dbmanager

    def create(self, name: str, profession: str, payment: float):
        self.dbmanager.insert((name, profession, payment))
        return True

    def read(self):
        fetch = self.dbmanager.select_all()
        return fetch

    def update(self, row_id: int, column_name: str, new_value: str | float):
        result = self.dbmanager.update(column_name, (new_value, row_id))
        return result > 0

    def delete(self, row_id: int):
        result = self.dbmanager.delete(row_id)
        return result > 0
