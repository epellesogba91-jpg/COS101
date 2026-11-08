#Input
name=input("Student Name: ")
while True:
    daily_trans=float(input("Daily Transport Cost: "))
    if daily_trans <0:
        print("Invalid Value, Try Again!")
        else:
            break
while True:
    daily_feed=float(input("Daily Feeding Cost: "))
    if daily_feed <0:
        print("Invalid Value, Try Again!")
        else:
            break
while True:
    days=int(input("Days on campus: "))
    if days <0:
        print("Invalid Value, Try Again!")
        else:
            break
while True:
    other_exp=float(input("Other Weekly Expenses: "))
    if days <0:
        print("Invalid Value, Try Again!")
        else:
            break
while True:
    other_exp=float(input("Other Weekly Expenses: "))
    if days <0:
        print("Invalid Value, Try Again!")
        else:
            break
while True:
    budget=int(input("Weekly Budget: "))
#Checking for Invalid Budget
    if budget <0:
        print("Invalid Number Please Try Again!")
        else:
            break
#Process
trans_tot=daily_trans*days
feed_tot=daily_feed*days
week_tot=trans_tot+feed_tot+other_exp
print()
if budget>week_tot:
    status="Exactly on Budget"
    print()
elif budget=week_tot:
    status="Over the Budget"
    print()
balance=budget-week_tot
print()
#Output
print()
print("\\\\\\\\\\\\\\\\\\")
print("Weekly Expenses Summary:")
print()
print("Student:",name)
print(Student:",name)
print("Transport Total:,format(trans_tot,".2f"))
print("Feeding Total:",format(feed_tot,".2f"))
print("Other Expenses:",format(other_exp,".2f"))
print("Weekly Total:",format(week_tot,".2f"))
print("Your total expense is", status)
print("Your Balance is", balance)
            
