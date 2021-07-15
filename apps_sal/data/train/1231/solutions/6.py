import sys
line = sys.stdin.readline()
n=int(line)
while n:
 try:
  line = sys.stdin.readline()
  t=int(line)
 except:
  break
 x=2**t
 sum=0
 while x:
  sum+=x%10
  x/=10
 print("\n%d"%sum)
 n-=1
