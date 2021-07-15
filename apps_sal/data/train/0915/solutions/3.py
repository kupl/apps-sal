# cook your dish here
t= int(input())
for _ in range(t):
 n= int(input())
 ls= list(map(int,input().split()))
 s = len(set(ls))
 print(s)

