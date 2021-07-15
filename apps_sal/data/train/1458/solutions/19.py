# cook your dish here
for _ in range(int(input())):
 n=int(input())
 cnt=0
 for i in range(1,n+1,2):
  s=n+1-i
  cnt=cnt+s*s
 print(cnt)

