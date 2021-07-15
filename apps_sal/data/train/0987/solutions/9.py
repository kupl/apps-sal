for _ in range(int(input())):
 # n = int(input())
 # arr = list(map(int,input().split()))
 fin,dx,acc,vel = list(map(int,input().split()))
 time = fin/vel
 tiger = 0.5*acc*time*time - dx
 if fin>tiger :
  print('Bolt')
 else :
  print('Tiger')

