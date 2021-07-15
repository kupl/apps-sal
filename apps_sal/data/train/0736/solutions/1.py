for t in range(int(input())):
 s = input()
 a = [0]*26
 for c in s:
  for i in range(26):
   a[i] += ord(c)-(ord('a')+i)
 m = float("inf")
 for i in a:
  m = min(m, abs(i))
 print(m)
