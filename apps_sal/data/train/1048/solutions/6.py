# cook your dish here
for i in range(int(input())):
 a,k=[int(i) for i in input().split()]
 l=[int(i) for i in input().split()]
 l=sorted(l)
 if(l[0]+a+2*k<=l[2]):
  print(0)
 elif(l[0]+2*k>=l[2]):
  print(a**2)
 else:
  p=l[2]-l[0]-2*k 
  print(a*(a-p))
  



