from datetime import date 
expenses=[]

def add_expense( expense_date=None):
    if expense_date is None:
        expense_date = date.today()
        amount=float(input("enter amount :-"))
        category= input("enter where you have spent :-")
    expenses.append({"amount": amount, "category": category, "date": expense_date})
def view_expenses():
    if not expenses:
        print("No expenses yet")
        return
    for i,e in enumerate(expenses,start=1):
        print(f"{i}.{e['category']}-{e['amount']}-{e['date']}")


def delete_expenses():
    view_expenses()
    if not expenses:
        return
    try:
        number=int(input("number to delete :"))
    except ValueError:
        print("Type a number")
        return
    if 1<= number <=len(expenses):
        expenses.pop(number-1)
        print("Deleted")
    else:
        print("Invalid number")	
def main():
    while True:
        print("\n1. Add\n2. View\n3.Delete\n4. Exit")
        choice =input("Choose:")
        if choice =="1":
            add_expense()
        elif choice =="2":
            view_expenses()	
        elif choice =="3":
            delete_expenses()
        elif choice =="4":
            print("goodbye!!!!")
            break
        else:
            print("Invalid choice")
main()
