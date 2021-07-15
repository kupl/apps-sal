t = int(input())
for i in range(t):
 s = input().rstrip()
 sumv = 0
 for j in range(len(s)):
  sumv += ord(s[j])
 minv = 10 ** 8;
 for i in range(ord('a'), ord('z') + 1):
  val = abs(sumv - i * len(s))
  if minv > val:
   minv = val
 print(minv)
