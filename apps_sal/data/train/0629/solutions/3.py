def potion(m, l):
 for _ in range(m):
  l.sort()
  l[2] = l[2] // 2
 return max(l)

try:
 tstc = int(input())
 for t in range(tstc):
  r, g, b, m = map(int, input().split())
  red = [int(i) for i in input().split()]
  green = [int(i) for i in input().split()]
  blue = [int(i) for i in input().split()]
  print(potion(m, [max(red), max(green), max(blue)]))
except:
 pass
