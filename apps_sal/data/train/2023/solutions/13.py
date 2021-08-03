from math import sqrt
n = int(input())
r = int(sqrt(n))
ans = []
if n == 1:
    print("1")
elif n == 2:
    print("1 2")
elif n == 3:
    print("1 3 2")
elif r ** 2 == n:
    for i in range(r):
        ans += [str((r - i - 1) * r + j) for j in range(1, r + 1)]
    print(" ".join(ans))
else:
    if n <= r * (r + 1):
        segment = r
        element = r + 1
    else:
        segment = r + 1
        element = r + 1
    for i in range(segment - 1):
        ans += [str(n - element * i - j) for j in range(element - 1, -1, -1)]
    ans += [str(j) for j in range(1, n - element * (segment - 1) + 1)]
    print(" ".join(ans))
