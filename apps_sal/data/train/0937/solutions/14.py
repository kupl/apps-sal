# cook your dish here
for t in range(int(input())):
 s=input()
 f=0
 for i in range(1,len(s)):
  if(s[i]<s[i-1]):
   f=1
   print("no")
   break
 if(f==0):
  print("yes")
