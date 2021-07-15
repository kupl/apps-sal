
for _ in range(int(input())):
 ranks = []
 lens = int(input())
 for i in range(lens):
  name = input()
  timing = int(input())
  ranks.append([name, timing])
 ranks = sorted(ranks, key = lambda x:x[1])
 for i in ranks:
  print(i[0])

