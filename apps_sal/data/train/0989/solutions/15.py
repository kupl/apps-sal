for _ in range(int(input())) :
 a, b, k = map(int,input().split())
 s = a + b + 1
 d = s // k
 if s % k != 0 :
  d += 1
 #print(d)
 if d % 2 == 1 :
  print("Chef")
 else :
  print("Paja")
