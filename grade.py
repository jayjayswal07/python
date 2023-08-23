print("calculating average marks of student of of 500 ")
sub1=int(input("enter marks in sub1 ="))
sub2=int(input("enter marks in sub2 ="))
sub3=int(input("enter marks in sub3 ="))
sub4=int(input("enter marks in sub4 ="))
sub5=int(input("enter marks in sub5 ="))

average=(sub1+sub2+sub3+sub4+sub5)/5

print("avearage of a student =",average)

print("now grade according to marks")

if average >90:
 print(" grade A")

elif(average >80 and average <90):
 print("grade B")
elif(average >70 and average <80):
 print("grade C")
elif(average >60 and average <70):
 print("grade D")
else:
       print("Below then 60 % is Fail")
