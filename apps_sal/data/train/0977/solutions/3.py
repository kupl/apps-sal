# cook your dish here
for _ in range(int(input())):
 n=int(input())
 a=input()
 s=""
 for i in range(1,n,2):
  s=s+a[i]+a[i-1]
 if n%2!=0:
  s=s+a[-1]
 d=""
 for i in s:
  a=219-ord(i)
  d=d+chr(a)
 print(d)

