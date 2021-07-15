testcases = int(input())
while testcases:
 p = int(input())
 Res = 1;
 n = 1;
 while n <= (2*p):
  Res = Res*n
  n = n+2
 print(Res)
 testcases=testcases-1

