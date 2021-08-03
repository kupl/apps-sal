import math
for _ in range(int(input())):
    lis = list(map(int, input().split()))
    n = lis[0]
    k = lis[1]
    temp = k * (k + 1) // 2
    if n < temp:
        print(-1)
    else:
        if k == 1:
            print(n)
        else:
            flag = 1
            for i in range(2, int(n**0.5) + 1):
                if (n % i == 0):
                    if(n // i >= temp):
                        flag = max(flag, i)
                    k = n // i
                    if(n // k >= temp):
                        flag = max(flag, k)
            print(flag)
'''
for _ in range(int(input())):
    n=int(input())
    lis=list(map(int,input().split()))
    q=int(input())
    s=''
    for i in range(n):
     if (lis[i]&1)==0:
      s+='0'
     else:
      s+='1'
    for _ in range(q):
     x=list(map(int,input().split()))
     l=x[0]
     r=x[1]
     temp='1'*((r+1)-l)
     if temp==s[l-1:r]:
      print("ODD")
     else:
      print("EVEN")
'''

'''
n=int(input())
lis=list(map(int,input().split()))
m=lis[0]
c=lis[1]
c1=0
c2=0
for i in range(n):
    temp=0
    t=list(map(int,input().split()))
    temp=t[1]-m*t[0]-c
    if temp>0:
     c1+=t[2]
    else:
     c2+=t[2]
print(max(c1,c2))
'''
