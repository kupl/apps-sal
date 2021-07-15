# cook your dish here
for i in range(int(input())):
 a=int(input())
 b=list(map(int,input().split()))
 b.sort()
 print(abs(sum(b[:a//2])-sum(b[a//2:])))
