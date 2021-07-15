# cook your dish here
t = int(input())

for _ in range(t):
 
 n = int(input())
 
 # ans = n*((n+1)**3)*0.5 - n*((n+1)**2)*(2*n+1)*(1/3) + (n*(n+1)*0.5)**2
 ans = n*(n+1)*(2*n +1)/6
 
 print(int(ans))
