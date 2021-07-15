import math
n = int(input())
a = sorted(map(int,input().split()))
l = [0]*n
for i in range(n):
 l[i] = a[i] + l[i-1]
for q in range(int(input())):
 print(l[int(math.ceil(float(n)/(int(input())+1)))-1])
