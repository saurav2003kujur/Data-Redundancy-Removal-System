from database import (
    create_table,
    insert_employee,
    email_exists
)

from validator import validate_data

from duplicate_detector import (
    check_exact_duplicate,
    check_false_positive
)

def add_employee():

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    department = input("Enter Department: ")

    valid, message = validate_data(
        name,
        email,
        phone
    )

    if not valid:
        print(message)
        return

    if email_exists(email):
        print("Duplicate Record Found")
        return

    duplicate, msg = check_exact_duplicate(
        email,
        phone
    )

    if duplicate:
        print(msg)
        return

    fp, fp_msg = check_false_positive(name)

    if fp:
        print(fp_msg)

    insert_employee(
        name,
        email,
        phone,
        department
    )

    print("Unique Record Added Successfully")

def main():

    create_table()

    while True:

        print("\n===== MENU =====")
        print("1. Add Employee")
        print("2. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()