
def __starting_point():
 a, b, c, d = sorted(map(int, input().split()))
 if d * a == b * c:
  print('Possible')
 else:
  print('Impossible')

__starting_point()
