name=input("Enter your name -")
age=int(input("age-"))
ticket=int(input("number of tickets-"))

if age in range(0,6):
 ticket_prize=0
 category='children'
 print("ticket is free")

elif age in range(6,18):
  ticket_prize=100
  category='student'
  print("ticket price is-",100*ticket)
  
else: 
 category='adult'
 ticket_prize=150
 print("ticket prize is- ",150*ticket)

total_prize=ticket*ticket_prize

print("\n_____ticket details_____")
print(name)
print(age)
print("no of ticket-",ticket)
print(category)
print("total prize is -",total_prize)