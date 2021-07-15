N=int(input())
count=0
while N!=0:
 count +=1
 N //=10
if count<=3:
 print(count)
else:
 print("More than 3 digits")
