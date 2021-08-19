for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    tot = n * (n + 1) // 2
    ans = a.copy()
    to_add = 0
    if n >= 62:
        print('NO')
        continue
    for i in range(n - 1):
        to_add = a[i]
        for j in range(i + 1, n):
            to_add = to_add | a[j]
            ans.append(to_add)
    if len(set(ans)) == tot:
        print('YES')
    else:
        print('NO')
