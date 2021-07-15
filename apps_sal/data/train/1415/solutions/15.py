def isp(s):
 return s==s[::-1]
for _ in range(int(input())):
 s=input()
 s=list(s)
 if s==s[::-1]:
  print('YES')
  continue 
 f=0 
 n=len(s)
 for i in range(n):
  if s[i]!=s[n-i-1]:
   ind=i 
   if isp(s[:ind]+s[ind+1:]):
    f=1 
   ind=n-i-1 
   if isp(s[:ind]+s[ind+1:]):
    f=1 

   break 
 print('YES' if f else 'NO')
