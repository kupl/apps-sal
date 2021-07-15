# cook your dish here
for _ in range(int(input())):
 s=input()
 s1=s2=s3=s4=s5=0
 for i in range(len(s)):
  if s[i]=='L':
   s1+=1
  if s[i]=='T':
   s2+=1
  if s[i]=='I':
   s3+=1
  if s[i]=='M':
   s4+=1
  if s[i]=='E':
   s5+=1
 if s1>=2 and s2>=2 and s3>=2 and s4>=2 and s5>=2 and len(s)>9:
  print("YES")
 elif s1>=2 and s2>=2 and s3>=2 and s4>=2 and s5>=1 and len(s)==9:
  print("YES")
 else:
  print("NO")
