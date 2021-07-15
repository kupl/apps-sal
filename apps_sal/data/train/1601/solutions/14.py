for _ in range(int(input())):
 n,p=map(int,input().split())
 d=n%(n//2+1)
 #print("d = ",d)
 if (n==2 or n==1):
  t=p*p*p
 else:
  t=(p-d)*(p-d)+(p-d)*(p-n)+(p-n)*(p-n)
 print(t)
