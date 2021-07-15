# cook your code here

T = int(input())

for t in range(T):
 N = int(input())
 C = [0] * N 
 score = [0] * N
 cookies = [ [0] * 7 for _ in range(N)]
 
 for i in range(N):
  
  inpt = input().split(' ')
 
  C[i] = int(inpt[0])
 
  for j in range(C[i]):
   k = int(inpt[j+1])
   cookies[i][k] = cookies[i][k]+1
  
  cookies[i].sort()
  
  six = cookies[i][1]
  five = cookies[i][2]
  four = cookies[i][3]
  
  five = max(0, five-six)
  four = max(0, four-six-five)
  score[i] = C[i] + 4*six + 2*five + 1*four
     
  
 tie = 0 
 maxscore = 0
 maxchef = 0
 for i in range(N):
  if score[i] > maxscore:
   maxscore = score[i]
   tie = 0
   maxchef = i
  elif score[i] == maxscore:
   tie = 1
 
 if tie > 0:
  print("tie")
 elif maxchef == 0:
  print("chef")
 else:
  print(maxchef+1)
  
  
 

