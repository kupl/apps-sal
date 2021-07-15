n = int(input())
while(n>0):
 s1,c1=input().split(" ")
 c1=int(c1)
 s1=list(set(s1))
 answer=""
 for c in range(97,123):
  if chr(c) in s1:
   if(c1>0):
    answer+=chr(c)
    c1=c1-1;
   else:
    continue 
  else:
   answer+=chr(c)
 if(len(s1)<=len(answer)):
  print(answer[:len(s1)])
 else:
  print("NOPE");
 n=n-1;
