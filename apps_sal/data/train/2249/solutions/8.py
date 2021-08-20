from sys import stdin
for _ in range(int(stdin.readline())):
    (x1, y1, x2, y2) = map(int, stdin.readline().split())
    ans = abs(x2 - x1) + abs(y2 - y1)
    if x1 != x2 and y1 != y2:
        ans += 2
    print(ans)
