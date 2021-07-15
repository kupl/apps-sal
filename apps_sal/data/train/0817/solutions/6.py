# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    l.sort()
    for i in range(n):
        s=s^l[i]
        #s=s^i
    print(s)        
