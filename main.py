from src.dbmanager import DbManager
from src.utils import validate_int, validate_float, menu
from src.crud import CRUD

while True:
    menu()
    choice = validate_int("What do you want to do?\n>> ")

    # VERIFY THE INTERVAL AND THE VALUE TYPE
    try:
        if 0 > choice or choice > 4:
            print("[ERROR] - Invalid value")
            continue
    except TypeError:
        print("[ERROR] - Choose between 0 and 4")
        continue

    crud = CRUD()
    dbmanager = DbManager()

    # PREVENTS EMPTY DATABASE PROBLEMS
    if choice > 1:
        if dbmanager.select("select * from users limit 1;", 2) is None:
            print("[INFO] - The table is empty")
            continue

    match choice:
        # EXIT
        case 0:
            print("Program finished")
            dbmanager.close()
            break
        # CREATE
        case 1:
            name = input("name: ")
            profession = input("Profession: ")
            payment = float(input("Payment: "))
            crud.create(name, profession, payment)

        # READ
        case 2:
            rows = crud.read()
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Profession: {row[2]}, Payment: R${row[3]:.2f}")

        # UPDATE
        case 3:
            row_id = validate_int("Row ID: ")
            if row_id is None:
                print('[ERROR] - Invalid ID')
                continue

            # PREVENTS WRONG "column_name"2
            column_name = input("Column name (name, profession, payment): ").lower()
            if column_name not in ["name", "profession", "payment"]:
                print("[ERROR] - Invalid column")
                continue

            # FOR 2 TYPES OF VALUES
            if column_name == "payment":
                new_value = validate_float("New value: ")
            else:
                new_value = input("New value: ")

            crud.update(row_id, column_name, new_value)

        # DELETE
        case 4:
             row_id = validate_int("Row ID: ")
             if row_id is None:
                 print("[ERROR] - Invalid ID")
                 continue
             crud.delete(row_id)
