# cook your dish here
import sys
import bisect
input=sys.stdin.readline
l=input().split()
n=int(l[0])
x=int(l[1])
y=int(l[2])
ok=[]
for i in range(n):
 l=input().split()
 li=[int(i) for i in l]
 ok.append(li)
l=input().split()
xi=[int(i) for i in l]
l=input().split()
yi=[int(i) for i in l]
xi.sort()
yi.sort()
mina=10**18
for i in range(n):
 num1=bisect.bisect_right(xi,ok[i][0])
 num2=bisect.bisect_left(yi,ok[i][1])
 if(num1>=1 and num2<y):
  mina=min(yi[num2]-xi[num1-1],mina)
print(mina+1)


