# cook your dish here
tests = int(input())
for _ in range(tests):
   s, sg, fg, d, t = [int(j) for j in input().split()]
   speed = s + 180 * d / t
   abs_s = abs(sg-speed)
   abs_f = abs(fg-speed)
   if abs_s < abs_f:
      print("SEBI")
   elif abs_f < abs_s:
      print("FATHER")
   else:
      print("DRAW")
