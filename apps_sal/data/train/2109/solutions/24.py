n = int(input())
l = []
for i in range(n):
    a, b = list(map(int, input().split()))

    p = int((a * b)**(1 / 2))

    if p * (p + 1) < a * b:
        ans = int(2 * p - 1)
    elif p**2 == a * b and not a == b:
        ans = int(2 * p - 3)
    else:
        ans = int(2 * p - 2)
    l.append(ans)

for i in range(n):
    print((l[i]))
