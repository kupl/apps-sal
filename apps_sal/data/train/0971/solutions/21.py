def change_it(_list):
 if(len(set(_list)) <= 2):
  return len(set(_list))-1
 k = []
 for i in range(len(_list)):
  r = _list.count(_list[i])
  k.append(r)
 s = max(k)
 return len(_list)-s


def __starting_point():
 t = int(input())
 for i in range(t):
  n = int(input())
  _list = list(map(int, input().split()))
  print(f'{change_it(_list)}')


__starting_point()
