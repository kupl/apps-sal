def make_div_3(a):
 d = {
  1 : [1, 4, 7],
  2 : [2, 5, 8]
 }
 rem = sum(a) % 3
 while rem:
  l1 = d[rem]
  i = sorted(list(set(a).intersection(l1)))
  if i:
   a.remove(i[0])
  else:
   l2 = d[2 if rem == 1 else 1]
   i = sorted(list(set(a).intersection(l2)))
   if i:
    a.remove(i[0])
   else:
    return -1
  rem = sum(a) % 3
 if len(a) == a.count(0):
  return [0]
 return a

def __starting_point():
 t = int(input())
 while t:
  n = int(input())
  a = [int(i) for i in input().split()]
  if not 0 in a:
   print(-1)
  else:
   sa = sorted(a)
   sa.reverse()
   a = make_div_3(sa)
   if a == -1:
    print(a)
   else:
    print(''.join([str(i) for i in a]))
  t -= 1

__starting_point()
