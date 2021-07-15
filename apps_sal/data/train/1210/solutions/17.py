# cook your dish here
t=int(input())
for _ in range(t):
 n,x=map(int,input().split())
 k,l=input().split()
 
 if k=="L":
  number=x
 else:
  number=n+1-x
 if number%2==0:
  if l=="H":
   lang="E"
  else:
   lang="H"
 else:
  lang=l
 print(number,lang)
