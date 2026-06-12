from database import get_all_employees

employees = get_all_employees()

for emp in employees:
    print(emp)