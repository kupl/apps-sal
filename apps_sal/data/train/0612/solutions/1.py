# cook your dish here
t=int(input())
for i in range(t):
 s=input()
 fl=-1
 n=len(s)
 for i in range(n-2):
  if(s[i:i+3]=="010" or s[i:i+3]=="101"):
   fl=0
   print("Good")
   break

 if(fl==-1):
  print("Bad")

