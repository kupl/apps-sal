from sys import stdin
n = int(stdin.readline())
d = {}
count = sm = 0
for num in map(int, stdin.readline().split()):
 sm += num
 if not sm: count += 1
 if sm in d:
  count += d[sm]
  d[sm] += 1
 else: d[sm] = 1
print(count)
