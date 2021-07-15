rd = lambda: list(map(int, input().split()))

rd()
a = sorted(rd(), reverse=True)
b = sorted(rd(), reverse=True)
if len(a) > len(b): print("YES"); return
for i in range(len(a)):
  if a[i] > b[i]: print("YES"); return
print("NO")
