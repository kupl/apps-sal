# cook your dish here
import itertools
t=int(input())
for i in range(t):
 n,k=list(map(int, input().split()))
 num=list(map(int,input().split()))
 y=list(itertools.combinations(num,k))
 num1=[]
 for i in range(len(y)):
  num1.append(sum(y[i]))
 x=min(num1)
 print(num1.count(x))
 

