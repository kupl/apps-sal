from sys import stdin
I=stdin.readline
for _ in range(int(I())):
 d=int(I())
 seq=[]
 if d==0:
  print(1)
  print(1)
  continue
 n=d//(10**5-2)
 rem=d%(10**5-2)
 seq=[10**5,10**5-1,1]*n
 seq.extend([rem+2,rem+1,1])
 if len(seq)>100000:
  print(runtme)
 print(len(seq))
 for i in range(len(seq)):
  if 1>seq[i]>100000:
   print(runtime)
  print(seq[i],end=" ")

 print("")

