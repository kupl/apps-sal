T = int(input())

for i in range(T):
 N = int(input())
 maxSpeeds = list(map(int, input().split()))
 
 travSpeeds = []
 
 for j in range(N):
  travSpeeds.append(maxSpeeds[j])
 
 for j in range(N - 1):
  if travSpeeds[j] < travSpeeds[j + 1]:
   travSpeeds[j + 1] = travSpeeds[j]
   
 maxSpeedCars = 0
 
 for j in range(N):
  if travSpeeds[j] == maxSpeeds[j]:
   maxSpeedCars += 1
   
 print(maxSpeedCars)
