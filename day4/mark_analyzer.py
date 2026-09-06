
name=input("enter the name")
marks=[]
for i in range(5):
    mark=int(input(f"enter the marks{i+1}"))
    marks.append(mark)

total=sum(marks)
print("total marks =",total)

average=sum(marks)/len(marks)
print("average marks =",average)

highest=max(marks)
print(highest)

lowest=min(marks)
print(lowest)

pass_count=0
fail_count=0

for mark in marks:
    if mark >=40:
        pass_count+=1
    else:
        fail_count+=1

    if average >= 90:
         grade = "A+"

    elif average >=80:
          grade="A"

          
    elif average >=70:
          grade="B"
          
    elif average >=60:
          grade="C"
          
    elif average >=50:
          grade="D"

    else:
         grade="F"
    if fail_count==0:
          result="PASS"

    else:
          result="FAIL" 


print("____-student performance____")
print("name -",name)
print("marks obtained  ",marks)
print("average ",average)
print("highest",highest)
print("lowest",lowest)
print("passed",pass_count)
print("failed",fail_count)
print("overall result",result)