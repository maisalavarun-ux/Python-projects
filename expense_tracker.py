
expenses = []

def show_menu():
    
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Exit")

def add_expense():
    name = input("Enter Your Name:")
    cost = float(input("Enter Your Expenses:"))

    expense = {
        "name" : name,
        "cost" : cost
    }

    expenses.append(expense)
    print("Expense added Successfully")

def view_expense():
    if(len(expenses) == 0):
        print("No expenses Found")
        return

    print("\n---Expenses---")
    x = 1
    for expense in expenses:
        print(f"{x}.{expense['name']}-₹{expense['cost']}")
        x += 1

def calc_expenses():
    total = 0

    for expense in expenses:
        total += expense["cost"]
    print(f"\nTotal Expenses :₹{total}")

print("-------Welcome to Expense Tracker-------")
show_menu()

while True:

    choice = input("Enter Your Task:")

    if (choice == "add"):
        add_expense()

    elif(choice == "view"):
        view_expense()

    elif(choice == "total"):
        calc_expenses()

    elif(choice == "exit"):
        print("Thanks For Using the Expense Tracker")
        break

    elif(choice == "menu"):
        show_menu()

    else:
        print("Invalid choice. Try Again.")
        




