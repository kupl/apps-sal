t=int(input())
for i in range(t):
 n=input()
 m=n.count('10')+n.count('01')
 if(n[-1]!=n[0]):
  m+=1
 print('uniform' if m<=2 else 'non-uniform')
 

