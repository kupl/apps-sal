for _ in range(int(input())):
 n = int(input())
 hsh = [0] * 9
 for _ in range(n):
  q, s = map(int, input().split())
  if q in range(1, 9):
   if hsh[q] < s:  hsh[q] = s

 print(sum(hsh))
