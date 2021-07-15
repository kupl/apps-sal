# cook your dish here
for _ in range(int(input())):
 n=int(input())
 a=[int(x) for x in input().split()]
 m=min(a)
 print(m*(n-1))
