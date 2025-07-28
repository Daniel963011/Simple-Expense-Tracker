import calendar
import datetime

from expenses import Expense

def main():
    print("Program is runnning .....................")

    expense_file_path = "expense.csv"
    budget = 2000

    #Get user to input expense
    expense = get_expense()
    
    #Write expense to file 
    save_expense(expense, expense_file_path)
    #Read file and create report
    sumarize(expense_file_path, budget)
    

def get_expense():
    print("Get User expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter the amount: "))
    print(f"You have entered {expense_name}, {expense_amount}")

    expense_category =[
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc."
    ]
    
    while True:
        print("Select category: ")
        for i, category_name in enumerate(expense_category):
            print(f" {i+1}. {category_name}")
        
        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_Expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_Expense
        else:
            print("Invalid entry")


def save_expense(expense: Expense, expense_file_path):
    print(f"Saving the user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f" {expense.name}, {expense.amount}, {expense.category}\n")
    

def sumarize(expense_file_path, budget):
    print(f"Summarize User expense: {expense_file_path}")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            #print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
                )
            expenses.append(line_expense)
            #print(line_expense)
    #print(expenses)

    #look up expense by categorgy by using dictionary
    amt_by_cat = {}

    for expense in expenses:
        key = expense.category
        if key in amt_by_cat:
            amt_by_cat[key] = amt_by_cat[key] + expense.amount
        else:
            amt_by_cat[key] = expense.amount

    #print(amt_by_cat)

    print("Expenses by category")
    for key,amount in amt_by_cat.items():
        print(f"    {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"Total spent {total_spent:.2f} this month!")

    remainder = budget - total_spent
    print(f"Budget remaining: ${remainder:.2f} this month!")

    
    #current date
    now = datetime.datetime.now()

    #number of days in current month
    daysInMonth = calendar.monthrange(now.year, now.month)[1]

    #remaining days in current month
    remainingDays = daysInMonth - now.day

    print(green(f"There are: {remainingDays} in the current month"))

    dailyBudget = remainder / remainingDays
    print(green(f"Budget per day is: ${dailyBudget}"))

#function to make numbers stand out
def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()