# cook your dish here
import math
test = int(input())

for _ in range(0,test):
 l,b = list(map(int,input().split()))
 num = math.gcd(l,b)
 print((l*b)//num**2)

