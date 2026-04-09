def validate_int(message):
    while True:
        try:
            return int(input(message))
        except (ValueError, TypeError):
            print("[ERROR] - Invalid Value")
            menu()
            continue

def validate_str(name, message):
    while True:
        text = input(message)
        if not text:
            print(f"[ERROR] - {name} cannot be empty")
            continue
        else:
            return text


def validate_float(message):
    while True:
        try:
            return float(input(message))
        except (ValueError, TypeError):
            print("[ERROR] - Invalid value")

def validate_column(message):
    while True:
        column_dict = {1: "name", 2: "profession", 3: "payment"}
        print("-"*20)
        for i in column_dict:
            print(f"{i} - {column_dict[i]}")
        print("-"*20)

        try:
            column_number = int(input(message))
            column = column_dict.get(column_number)

            if not column:
                print("[ERROR] - Invalid column")
                continue
            else:
                return column

        except (ValueError, TypeError):
            print("[ERROR] - Invalid Value")


def menu():
    to_do = ["1 - Create", "2 - Read", "3 - Update", "4 - Delete", "0 - Exit"]
    print("\n" + "-" * 20)
    print("CRUD MENU".center(20))
    print("-" * 20)
    for i in to_do:
        print(i)
    print("-" * 20)
