for _ in range(int(input())):
 v1,t1,v2,t2,v3,t3=map(int,input().split())
 if v1+v2<v3 or t3<t1 or t3>t2:
  print('NO')
  continue
 p = v3*((t3-t1)/(t2-t1))
 q = v3*((t2-t3)/(t2-t1))
 if 0<=q<=v1 and 0<=p<=v2:
  print('YES')
 else:
  print('NO')
