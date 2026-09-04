number=int(input("enter a number"))

total=0
even_count=0
odd_count=0
print("______NUMBER ANALYZER_____")

for i in range(1,number+1):

    if i%2==0:
        print("the number ",i," is even")
        even_count=even_count+i

    else:
        print("the number ",i," is odd")
        odd_count=odd_count+i

        
total=total+i

print("total-",total)
print("odd-",odd_count)
print("even -",even_count)

