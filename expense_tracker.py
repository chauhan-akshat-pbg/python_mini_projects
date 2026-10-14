from datetime import date 
expenses=[]

def add_expense( expense_date=None):
	if expense_date is None:
		expense_date = date.today()
		amount=float(input("enter amount :-"))
		category= input("enter where you have spent :-")
	expenses.append({"amount": amount, "category": category, "date": expense_date})
print(expenses)
add_expense()
print(expenses)
add_expense()
print(expenses)
