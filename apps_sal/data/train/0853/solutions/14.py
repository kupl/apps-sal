import collections
for _ in range(int(input())):
 playerSize = int(input())
 player = []
 values = []
 newValues = []
 for i in range(playerSize):
  player.append(input())
  values.append(int(input()))
 newValues = sorted(values)
 #print(values)
 #print(player)
 #print(newValues)
 for i in range(playerSize):
  for j in range(playerSize):
   if newValues[i]==values[j]:
    print(player[j])
