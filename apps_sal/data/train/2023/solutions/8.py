import math
n = int(input())
wk1 = math.floor(math.sqrt(n))
wk2 = n // wk1
for i in range(wk2 * (wk1), n):
    print(i + 1, end=" ")
for i in reversed(range(wk1)):
    for j in range(wk2 * i, wk2 * (i + 1)):
        print(j + 1, end=" ")
print()
