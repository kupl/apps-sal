n = int(input())
m = []
if n <= 18:
    a = 0
else:
    a = n - len(str(n)) * 9
for i in range(a, n):
    x = i
    for j in str(i):
        x += int(j)
    if n == x:
        m.append(i)
print(len(m))
[print(i) for i in m]
