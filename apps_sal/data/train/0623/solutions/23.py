# cook your dish here
x=int(input())
lst=[]
for i in range(0,x): 
     y=int(input()) 
     lst.append(y)
lst.sort()
for i in range(0,x):
     print(lst[i])

