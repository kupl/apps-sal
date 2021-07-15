# cook your dish here
from sys import stdin,stdout
a,b=list(map(int,stdin.readline().split()))
left=[]
top=[]
for i in range(a):
 c,d=list(map(int,stdin.readline().split()))
 left.append(c)
 top.append(d)
left.sort()
top.sort()
from bisect import bisect_right as br
from bisect import bisect_left as bl
row=0
col=0
total=0
cons_x=0
cons_y=0
for i in range(len(left)):
 cons_x+=(abs(left[i]))
 cons_y+=(abs(top[i]))
total=cons_x+cons_y
cc=stdin.readline().rstrip()
for i in cc:
 if i=="R":
  kk=br(left,col)
  cons_x=(cons_x+kk-(a-kk))
  col+=1
 if i=="L":
  kk=bl(left,col)
  cons_x=(cons_x+(a-kk)-kk)
  col-=1
 if i=="U":
  kk=br(top,row)
  cons_y=(cons_y+kk-(a-kk))
  row+=1
 if i=="D":
  kk=bl(top,row)
  cons_y=(cons_y+(a-kk)-kk)
  row-=1
 stdout.write(str(cons_x+cons_y))
 stdout.write("\n")
  


