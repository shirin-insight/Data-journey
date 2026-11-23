employees = {
    "Ali": {
        "sales": 45,
        "target": 50,
        "salary": 12000
    },
    "Sara": {
        "sales": 75,
        "target": 60,
        "salary": 15000
    },
    "Reza": {
        "sales": 30,
        "target": 40,
        "salary": 10000
    },
    "Mina": {
        "sales": 90,
        "target": 80,
        "salary": 18000
    },
    "Nima": {
        "sales": 55,
        "target": 50,
        "salary": 13000
    }
}
total = 0
targeted_employee = ""
max_sale = 0
best_employee = ""
low_level_employee = ""
for employee in employees:
    total = total + employees[employee]["sales"]
    if employees[employee]["sales"] >= employees[employee]["target"]:
        targeted_employee = employee
        print("targeted_employee:",targeted_employee)
    if employees[employee]["sales"] > max_sale:
        max_sale = employees[employee]["sales"]
        best_employee = employee
        print("best_employee:",best_employee)
    if employees[employee]["sales"] < 40:
        low_level_employee = employee
        print("low_level_employee:",low_level_employee)
average = total / len(employees)
print("total:",total)
print("average: ",average)




