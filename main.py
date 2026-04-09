from src.utils import validate_int, validate_float, menu
from src.crud import CRUD

while True:
    menu()

    choice = validate_int("What do you want to do?\n>> ")

    if 0 > choice or choice > 4:
        print('[ERROR] - Invalid value')
        continue

    crud = CRUD()
    crud.create_table()

    if choice > 1:
        if crud.is_content() is None:
            print("[INFO] - The table is empty")
            continue

    match choice:
        case 0:
            print('Program finished')
            crud.close()
            break
        case 1:
            name = input('name: ')
            profession = input('Profession: ')
            payment = float(input('Payment: '))
            crud.create(name, profession, payment)

        case 2:
            rows = crud.read()
            for row in rows:
                print(f'ID: {row[0]}, Name: {row[1]}, Profession: {row[2]}, Payment: R${row[3]:.2f}')
                # print(row)

        case 3:
            row_id = validate_int("Row ID: ")
            if row_id is None:
                print('[ERROR] - Invalid ID')
                continue

            column_name = input("Column name (name, profession, payment): ").lower()
            if column_name not in ["name", "profession", "payment"]:
                print('[ERROR] - Invalid column')
                continue

            if column_name == "payment":
                new_value = validate_float("New value: ")
            else:
                new_value = input("New value: ")

            crud.update(row_id, column_name, new_value)

        case 4:
            row_id = validate_int("Row ID: ")
            if row_id is None:
                print('[ERROR] - Invalid ID')
                continue
            crud.delete(row_id)
            pass
