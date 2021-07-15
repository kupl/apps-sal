# cook your dish here
try:
    t=int(input())
    for i in range(0,t):
        l=[]
        a,b,c=map(int,input().split())
        l.append(a)
        l.append(b)
        l.append(c)
        w=max(l)
        l.remove(w)
        w=max(l)
        print(w)
except:pass
