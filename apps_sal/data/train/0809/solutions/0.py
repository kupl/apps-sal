#from itertools import combinations as c
n=int(input());l=list(map(int,input().split()))
l1=[]
if(n<3):
    print("NO")
else:
    l.sort()
    for i in range(n-2):
        if(l[i]+l[i+1]>l[i+2]):
            l1.append([l[i+2],l[i+1],l[i]])
if(len(l1)!=0):
    print("YES")
    print(*max(l1))
else:
    print("NO")
