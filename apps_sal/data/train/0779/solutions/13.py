# cook your dish here
def poison(n,concentration):
 
 concentration=sorted(concentration)
 for i in range(n-1,0,-1):
  replaced=(concentration[i]+concentration[i-1])/2
  concentration.pop()
  concentration.pop()
  concentration.append(replaced)
  
 return concentration[0]



t=int(input())
for i in range(t):
 n=int(input())
 concentration=[int(x) for x in input().split()]
 ans=poison(n,concentration)
 print('%.6f'%ans)
