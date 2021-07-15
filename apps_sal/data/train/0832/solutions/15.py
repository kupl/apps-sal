# cook your dish here
import itertools
t=int(input())
for i in range(t):
 n,k=map(int, input().split())
 num=list(map(int,input().split()))
 y=list(itertools.combinations(num,k))
 num1=[]
 for i in range(len(y)):
  num1.append(sum(y[i]))
 print(num1.count(min(num1)))
