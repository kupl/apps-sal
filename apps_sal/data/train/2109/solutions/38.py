import math
q = int(input())
for i in range(q):
    (a, b) = list(map(int, input().split()))
    c = int(math.sqrt(a * b))
    ans = 2 * (c - 1)
    if (a * b - 1) // c > c:
        ans += 2
    elif a * b == c * c:
        pass
    else:
        ans += 1
    if not a == b == c:
        ans -= 1
    print(max(0, ans))
