from collections import Counter

for _ in range(int(input())):
 N = int(input())
 max_points = [-1, [-1]]
 for player in range(N):
  data = input().split()
  storage_distinct = Counter(data[1:])
  points = int(data[0])
  
  while len(storage_distinct) >= 4:
   if len(storage_distinct) == 4:
    points += 1
   elif len(storage_distinct) == 5:
    points += 2
   elif len(storage_distinct) >= 6:
    points += 4
    
   for i in list(storage_distinct.keys()):
    storage_distinct[i] -= 1
    if storage_distinct[i] == 0:
     del storage_distinct[i]
  
  if points > max_points[0]:
   max_points[0] = points
   max_points[1] = [player]
  elif points == max_points[0]:
   max_points[1].append(player)
   
 if len(max_points[1]) > 1:
  print("tie")
 elif max_points[1][0] == 0:
  print("chef")
 else:
  print(max_points[1][0] + 1)
