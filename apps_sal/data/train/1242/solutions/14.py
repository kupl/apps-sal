# cook your dish here
for i in range(int(input())):
 n=int(input())
 lis=list(map(int,input().split()))
 print(min(lis)*(n-1))
