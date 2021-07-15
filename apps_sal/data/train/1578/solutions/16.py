c=1
cases=eval(input())

while(c<=cases):
 s=list(input())
 sumc=0
 for i in s:
  g=ord(i)
  if(g>48 and g<=57):
   sumc+=int(i)
 print(sumc)
 c=c+1
