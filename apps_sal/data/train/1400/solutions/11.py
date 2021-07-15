for _ in range(int(input())):
 def n_th_term(r):
  return 2**(r-1)
 p=list(map(int,input().split()))
 n=p[0]
 l=p[1]
 r=p[2]
 maximum=2**(r)-1+(n-r)*n_th_term(r)
 minimum=2**(l)-1+(n-l)
 print(f"{minimum} {maximum}")
 

