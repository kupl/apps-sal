import math
n,r=list(map(int,input().split()))
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    a.append(abs(r-l[i]))
num1=a[0]
num2=a[1]
gcd=math.gcd(num1,num2)
for i in range(2,len(a)):
    gcd=math.gcd(gcd,a[i])
print(gcd)

