tcases=int(input())
lis=[]
for i in range(tcases):
 peoples=int(input())
 tells=list(map(int,input().split(" ")))
 lis.append((peoples,tells))
def days(x):
 tell=x[1]
 people=x[0]
 know=tell[0]
 add=tell[0]
 day=1
 if tell[0]+1>=people:
  return 1
 while know+1<people: 
  m=0
  for i in range(know-add+1,know+1):
   m+=tell[i]
   know+=tell[i]
  know+=add
  add+=m
  day+=1
 return day
for i in lis:
 print(days(i))
