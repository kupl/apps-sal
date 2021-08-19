import math
for _ in range(int(input())):
    lis = list(map(int, input().split()))
    n = lis[0]
    k = lis[1]
    temp = k * (k + 1) // 2
    if n < temp:
        print(-1)
    elif k == 1:
        print(n)
    else:
        flag = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if n // i >= temp:
                    flag = max(flag, i)
                k = n // i
                if n // k >= temp:
                    flag = max(flag, k)
        print(flag)
'\nfor _ in range(int(input())):\n    n=int(input())\n    lis=list(map(int,input().split()))\n    q=int(input())\n    s=\'\'\n    for i in range(n):\n     if (lis[i]&1)==0:\n      s+=\'0\'\n     else:\n      s+=\'1\'\n    for _ in range(q):\n     x=list(map(int,input().split()))\n     l=x[0]\n     r=x[1]\n     temp=\'1\'*((r+1)-l)\n     if temp==s[l-1:r]:\n      print("ODD")\n     else:\n      print("EVEN")\n'
'\nn=int(input())\nlis=list(map(int,input().split()))\nm=lis[0]\nc=lis[1]\nc1=0\nc2=0\nfor i in range(n):\n    temp=0\n    t=list(map(int,input().split()))\n    temp=t[1]-m*t[0]-c\n    if temp>0:\n     c1+=t[2]\n    else:\n     c2+=t[2]\nprint(max(c1,c2))\n'
