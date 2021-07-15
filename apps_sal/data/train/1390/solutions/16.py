# cook your dish here
for a0 in range(int(input())):
 n,q=list(map(int, input().split()))
 print(q*(n+q+1)/(q+1))
