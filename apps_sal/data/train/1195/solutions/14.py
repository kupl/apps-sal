for _ in range(int(input())) :
 n, a, b, c, d, p, q, y = list(map(int, input().split()))
 x = list(map(int, input().split()))
 walk = (abs(x[a-1] - x[b-1])) * p
 train = (abs(x[a-1] - x[c-1])) * p
 if train <= y :
  walk_train = y + (abs(x[d-1] - x[b-1])) * p + (abs(x[d-1] - x[c-1])) * q
  print(min(walk, walk_train))
 else :
  print(walk)
 

