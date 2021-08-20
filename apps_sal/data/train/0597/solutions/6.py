"""a,b,c=map(int,input().split())
if a-b>>31 and a-c>>31:
    print(a)
elif b-c>>31 and b-a>>31:
    print(b)
else:
    print(c)"""
"n=int(input())\nc=0\na=[i for i in range(1,n+1)]\nfor i in range(n-1):\n    for j in range(i,n):\n     if a[i]^a[j]>n:\n      c+=1\n      print('('+str(i+1)+','+str(j+1)+')')\nprint(c)"
"l=[0 for i in range(64)]\na=[str(i) for i in range(10)]+[chr(j) for j in range(65,91)]+[chr(k) for k in \xa0\xa0\xa0\xa0range(97,123)]+['-','_']\n\nfor i in range(64):\n    count=0\n    for j in range(64):\n     if i&j==i:\n      count+=1\n    l[i]=2*count-1\nprint(l)\n\nfor _ in range(int(input())):\n    s=input()\n    res=1\n    for i in s:\n     res*=l[a.index(i)]\n    print(res%1000000007)"
for _ in range(int(input())):
    n = int(input())
    X = [0 for i in range(n)]
    H = [0 for i in range(n)]
    for i in range(n):
        (x, h) = list(map(int, input().split()))
        X[i] = x
        H[i] = h
    X1 = [0 for i in range(n)]
    for i in range(n - 2):
        X1[i] = X[i + 2] - X[i]
    (X1[n - 2], X1[n - 1]) = (X[1] - X[0], X[n - 1] - X[n - 2])
    X1.sort()
    H.sort()
    res = 0
    for i in range(n):
        res += X1[i] * H[i]
    print(res)
