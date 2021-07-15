n=int(input())
mylist=[]
while n>0:
    num=input()
    count=0
    for i in num:
        if i=='4':
            count+=1
    mylist.append(count)
    n=n-1
for i in mylist:
    print(i)
           

