from src.crud import CRUD

def validate_int(message):
    try:
        number = int(input(message))
        return number
    except ValueError:
        print("[Error] - Invalid value")
        return

def validate_float(message):
    try:
        number = float(input(message))
        return number
    except ValueError:
        print("[Error] - Invalid value")
        return

def menu():
    to_do = ['1 - Create', '2 - Read', '3 - Update', '4 - Delete', '0 - Exit']
    print("CRUD".center(20))
    print("-" * 20)
    for i in to_do:
        print(i)
    print("-" * 20)

