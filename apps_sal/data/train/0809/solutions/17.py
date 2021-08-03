from sys import stdin, stdout
for _ in range(1):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    ans = []
    for x, y, z in zip(a, a[1:], a[2:]):
        if (x + y > z and x + z > y and y + z > x):
            ans = [x, y, z]
            break
    if not ans:
        print('NO')
    else:
        print('YES')
        print(*ans)
