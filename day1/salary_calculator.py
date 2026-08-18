name=(input("enter your name"))
age=int(input("age"))
place=(input("enter your place"))

monthly_salary = int(input("enter your salary"))
monthly_expense = int(input("enter your expense"))

year_salary = monthly_salary*12
year_expense = monthly_expense*12
savings=year_salary-year_expense


print(f"{name}-{age}-{place}")
print("yearly salary is",year_salary)
print("yearly expense is",year_expense)
print("savings in the year is",savings)