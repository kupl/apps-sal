# cook your dish here
import sys
R = lambda :list(map(int,input().split()))
t = int(input())
for _ in range(t):
 string = input()
 n = len(string)
 a = [0]*26
 for i in string:
  a[ord(i)-ord('A')]+=1
 rev_lst = sorted(a,reverse=True)
 ans = n
 for i in range(1,27):
  if n%i==0:
   x = int(n/i)
   y = 0
   for j in range(0,i):
    y+=min(rev_lst[j], x)
   ans = min(ans,n-y)

 print(ans)


