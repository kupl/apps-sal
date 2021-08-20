q = int(input())
for i in range(q):
    (x, y) = map(int, input().split())
    if x == y:
        print(2 * (x - 1))
        continue
    z = int((x * y) ** 0.5)
    if z ** 2 == x * y:
        z -= 1
    ans = 2 * z - 2
    if z * (z + 1) < x * y:
        ans += 1
    print(ans)
