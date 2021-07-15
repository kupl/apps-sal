# cook your dish here
from fractions import gcd
from functools import reduce

t=int(input())
for i in range(0,t):
 n=int(input())
 arr=list(map(int,input().split()))
 res= reduce(gcd, arr)
 res1= sum(arr)//res 
 print(res,res1)

