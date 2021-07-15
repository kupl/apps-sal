# cook your dish here
tests = int(input())
for test in range(tests):
 n = int(input())
 a = [int(x) for x in input().split()]
 maxx = max(set(a), key = a.count)
 moves = a.index(maxx)
 if len(a) > 1:
  for i in range(moves+1, len(a)):
   if a[i] != maxx:
    moves += 1
 print(moves)

