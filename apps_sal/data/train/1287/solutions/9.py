# cook your dish here
t=int(input())
for _ in range(t):
 s=input()
 s1=[]
 
 for i in range(len(s)):
  if s[i]=='a'or s[i]=='e'or s[i]=='i' or s[i]=='o' or s[i]=='u':
   s1.append(1)
  else:
   s1.append(0)
 s2=''.join([str(elem) for elem in s1]) 
 
 print(int(s2,2))
   

