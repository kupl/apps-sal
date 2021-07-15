for tests in range(int(input())):
 n = int(input())
 blockHeights = [int(blockHeight) for blockHeight in input().split()]
 sumOfBlockHeightsBefore = sum(blockHeights)
 blockHeights[0] = blockHeights[n-1] = 1

 # make all possible temples and choose biggest one, as its demolition cost         will be heighest
 # carve first half of temples i.e left right angle triangle, considering         temple an equilateral triangle
 for i in range(1, n):
  if blockHeights[i] > blockHeights[i-1] + 1:
   blockHeights[i] = blockHeights[i-1] + 1

 # carve second half of temples i.e right right angle triangle
 for i in range(n-2, -1, -1):
  if blockHeights[i] > blockHeights[i+1] + 1:
   blockHeights[i] = blockHeights[i+1] + 1
 heightOfTallestTemple = max(blockHeights)

 # find sum of blocks for height of tallest temple
 # through arithematic progression we have a1= 1, an = heightOfTallestTemple,         d = 1 and thus Sn = (a1 + an) * an / 2
 # so we have to AP series for two halves of temple
 # s1 = (1 + heightOfTallestTemple) * heightOfTallestTemple / 2
 # s2 = (1 + heightOfTallestTemple-1) * (heightOfTallestTemple - 1) / 2
 # s = s1 + s2
 # fruther simplifying we have
 # s = heightOfTallestTemple * heightOfTallestTemple
 s = heightOfTallestTemple ** 2

 noOfOperations = sumOfBlockHeightsBefore - s
 # print(blockHeights, heightOfTallestTemple, sum(blockHeights),         sumOfBlockHeightsBefore, s, sep=' | ')
 print(noOfOperations)

