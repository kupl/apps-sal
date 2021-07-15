a=input().split()
n=int(input())
for i in range(n):
    print(a[0],a[1])
    s1,s2=input().split()
    a[a.index(s1)]=s2
print(a[0],a[1])
