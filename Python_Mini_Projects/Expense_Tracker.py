print("---Expense Tracker---")

num_expenses = int(input("Enter number of expenses: "))

expenses = []
amounts = []

for i in range(num_expenses):
    expense = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append(expense)
    amounts.append(amount)

print("\n--- Expense Summary ---")

for i in range(num_expenses):
    print(expenses[i], ":", amounts[i])

total = sum(amounts)

print("Total Expenses:", total)