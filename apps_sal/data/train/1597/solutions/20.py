import sys
def input(): return sys.stdin.readline().strip()

t = int(input())
while t:
 t -= 1
 a, m = map(int, input().split())
 possible = []
 for i in range(2, int(m**0.5)+1):
  if not m%i:
   d = m//i
   if not (m-d)%(a*d):
    possible.append((m-d)//a)
   d = m//d
   if not (m-d)%(a*d):
    possible.append((m-d)//a)
 if not(m-1)%a:
  possible.append((m-1)//a)
  
 possible.sort()
 print(len(possible))
 for i in possible:
  print(i, end = " ")
 print()

