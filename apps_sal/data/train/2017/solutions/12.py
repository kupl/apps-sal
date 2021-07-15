n=int(input())
l=list(map(int,input().split(" ")))
a,c=0,0
while (l):
    a=l[0]
    l.remove(a)
    c+=l.index(a)
    l.remove(a)
print(c)
