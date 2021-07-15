from math import *
for u in range(int(input())):
    p=input()
    n=int(input())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    s=0
    l.sort(key=lambda x: [x[0],-x[1]])
    for i in range(1,n):
        s+=sqrt((l[i][0]-l[i-1][0])**2+(l[i][1]-l[i-1][1])**2)
    print('{0:.2f}'.format(s))

