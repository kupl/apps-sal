# cook your dish here
# cook your dish here
for j in range(int(input())):
 a=int(input())
 q=input()
 r=input()
 if q==r:
  print("Yes")
 else:
  c=0
  if(q.count('0')==r.count('0')):
   i=0
   while(i<a-1):
    if q==r:
     break
    if q[i]!=r[i]:
     if q[i]=='0':
      c=0
      break
     else:
      w=q[i+1:]
      k=w.index('0')
      q=q[:i]+q[i+k+1]+q[i+1:i+k+1]+q[i]+q[i+k+2:]
      i+=1
      c+=1
    else:
     i+=1
  if c==0:
   print("No")
  else:
   print("Yes")

