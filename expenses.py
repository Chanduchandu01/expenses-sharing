import sqlite3

cons = sqlite3.connect("expenses.db")

point = cons.cursor()

point.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY ,
Date DATE ,
explanation TEXT ,
category  TEXT ,
price REAL)""")

cons.commit()
cons.close()
import sqlite3

cons= sqlite3.connect("expenses.db")
point = cons.cursor()

while True:
  print("Select any one option:")
  print("1.Enter a expense")
  print("2.View all expenses")
  choice = int(input())
  if choice == 1:
    date = input("Enter the date of the expenses (YYYY-MM-DD): ")
    description = input("Enter the description of the expense: ")
    point.execute("SELECT DISTINCT category FROM expenses")
    categories = point.fetchall()
    print("Select a category by number:")
    for idx,category in enumerate(categories):
       print(f"{idx +1},{category[0]}")
    print(f"{len(categories) +1}.Create a new category")
    category_choice=int(input())
    if category_choice==len(categories)+1:
       category=input("enter the new category name: ")
    else:
       category=categories[category_choice-1][0]
    price=input("enter the price of the expense: ")
    point.execute("INSERT INTO expenses (Date,description,category,price) VALUES (?,?,?,?)",(date,description,category,price))
    cons.commit()
  elif choice==2:
    print("Select valid option:")
    print("1.View all expenses")
    print("2.View every month expenses by category")
    view_choice=int(input())
    if view_choice==1:
       point.execute("SELECT*FROM expenses")
       expenses=point.fetchall()
       for expense in expenses:
          print(expense)
    elif view_choice==2:
       month=input("enter the month (MM): ")
       year=input("enter the year (YYYY): ")
       point.execute("""SELECT category,SUM(price) FROM expenses"
                   WHERE strftime('%m',Date)=? AND strftime('%Y',Date)=?
                   GROUP BY category""",(month,year))
       expenses=point.fetchall()
       for expense in expenses:
          print(f"Category:{expense[0]},Total:{expense[1]}")
    else:
       exit()
  else:
    exit()
  repeat = input("Would you like to continue (y/n)?\n")
  if repeat.lower() !="y":
    break
cons.close()
bill=int(input("enter the total of bill: "))
tip=int(input("enter the percentage of tip? 5,10,12: "))
people=int(input("how many people to divide the bill: "))
tip_as_percentage=tip/100
total_tip=bill*tip_as_percentage
total_bill=bill+total_tip
bill_per_head=total_bill/people
final_amount=round(bill_per_head,2)
print(f"each person need to pay:Rs {final_amount}")
