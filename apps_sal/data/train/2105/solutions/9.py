n = int(input())
r = [1 for i in range(n + 2)]
for i in range(2, n + 2):
    if r[i] == 1:
        for j in range(i * i, n + 2, i):
            r[j] = 2
if n < 3:
    print(1)
else:
    print(2)
print(*r[2:])
