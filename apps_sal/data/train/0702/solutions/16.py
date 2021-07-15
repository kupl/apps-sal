try:
 for _ in range(int(input())):
  m,t1,t2=list(map(int,input().split()))
  t=t2-t1
  if(t%3==0):
   if(m>=(t//3)):
    print("No")
   else:
    print("Yes")
  else:
   print("Yes")
except EOFError as e:
 pass

