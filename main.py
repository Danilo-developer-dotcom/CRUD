from src.dbmanager import DbManager
from src.utils import validate_int, validate_float, menu, validate_column, validate_str
from src.crud import CRUD

dbmanager = DbManager()
crud = CRUD(dbmanager)

while True:
    menu()
    choice = validate_int("What do you want to do?\n>> ")

    # VERIFY THE INTERVAL
    if choice < 0 or choice > 4:
        print("[ERROR] - Choose between 0 and 4")
        continue


    # PREVENTS EMPTY DATABASE PROBLEMS
    if choice > 1:
        if dbmanager.select_one() is None:
            print("[ERROR] - The table is empty")
            continue

    match choice:
        # EXIT
        case 0:
            print("Program finished")
            dbmanager.close()
            break
        # CREATE
        case 1:
            name = validate_str("name")
            profession = validate_str("profession")
            payment = validate_float("payment: ")
            crud.create(name, profession, payment)
            print("[OK] - Values entered successfully")

        # READ
        case 2:
            rows = crud.read()
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Profession: {row[2]}, Payment: R${row[3]:.2f}")

        # UPDATE
        case 3:
            row_id = validate_int("Row ID: ")

            # PREVENTS WRONG "column_name"
            column_name = validate_column("Column id: ")

            # FOR 2 TYPES OF VALUES
            if column_name == "payment":
                new_value = validate_float("New value: ")
            else:
                new_value = validate_str(column_name.capitalize())

            if crud.update(row_id, column_name, new_value):
                print("[OK] - Values updated")
            else:
                print("[ERROR] - No values updated")

        # DELETE
        case 4:
            row_id = validate_int("Row ID: ")
            if crud.delete(row_id):
                print(f"[OK] - Row {row_id} deleted")
            else:
                print(f"[ERROR] - Row {row_id} not found")
                continue
