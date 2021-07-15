t = eval(input())
while(t):
 s1 = input()
 s2 = input()
 s1 = s1.lower()
 s2 = s2.lower()
 if s1<s2:
  print("first")
 elif s1>s2:
  print("second")
 else:
  print("equal")
 t = t - 1
