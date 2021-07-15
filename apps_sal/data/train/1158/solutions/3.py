import sys

n = int(sys.stdin.readline())

count = 0
def is_ciel(s):
 for i in '0124679':
  if s.count(i) > 0:
   return False
 if s.count('8') >= s.count('5') >= s.count('3'):
  return True
 return False


for _ in range(n):
 s = sys.stdin.readline().split()
 if is_ciel(s[-1]):
  count += 1

print(count)
