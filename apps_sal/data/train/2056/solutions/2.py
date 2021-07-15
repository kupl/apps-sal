def read():
    return [c == '1' for c in input()]
n = int(input())
a, b = read(), read()

res = 0

i = 0
while i + 1 < n:
    if a[i] != b[i] and a[i] != a[i+1] and b[i] != b[i+1]:
        a[i] = b[i]
        a[i+1] = b[i+1]
        res += 1
        i += 2
    else:
        i += 1

for i in range(n):
    if a[i] != b[i]:
        res += 1

print(res)
