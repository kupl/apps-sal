# cook your dish here
try:
 for i in range(int(input())):
  l=list(map(int,input().strip().split()))
  s=input()
  s=list(s)
  alpha="abcdefghijklmnopqrstuvwxyz"
  alpha=list(alpha)
  count=0
  for i in alpha:
   if i not in s:
    count=count+l[ord(i)-97]
  print(count)
except:
 pass

