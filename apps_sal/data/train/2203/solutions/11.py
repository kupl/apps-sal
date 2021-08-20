n = int(input())
pole = []
for i in range(n):
    s = list(map(int, input().split()))
    pole.append(s)
ans = [0] * n
for number in range(1, n + 1):
    for i in range(n):
        s = set()
        for j in range(n):
            if pole[i][j] > number - 1:
                s.add(pole[i][j])
        if len(s) == 1:
            for k in s:
                ans[i] = k
for i in range(n):
    if ans[i] == n - 1:
        ans[i] = n
        break
print(*ans)
