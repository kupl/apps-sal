def gcd(a, b):
 if b == 0:
  return a
 return gcd(b, a%b)

def gcd_of_list(lst):
 a = lst[0]
 for item in lst:
  a = gcd(item, a)
  if a == 1:
   return 1
 return a

def __starting_point():
 cases = int(input())
 for _ in range(cases):
  cuts = int(input())
  angles = list(map(int, input().split()))
  min_angle = angles[0]
  size = []
  for i in range(cuts):
   if i != cuts-1:
    size.append(angles[i+1]-angles[i])
  size.append(360-angles[-1]+angles[0])
  diff = gcd_of_list(size)
  print(360//diff - len(size))

__starting_point()
