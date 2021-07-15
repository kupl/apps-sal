t=int(input())
lst=[]
for m in range(t):
    n=int(input())
    lst.append(n)
l=[]
for i in range(0,len(lst)):
    count=0
    for j in range(0,i):
        if(lst[i]<lst[j]):
            count=count+1
    l.append(count+1)
for k in l:
    print(k)
