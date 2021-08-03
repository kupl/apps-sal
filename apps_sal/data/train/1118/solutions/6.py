def solve(s, n):
    ans = 0

    for i in range(n):
        if i % 2 == 0 and s[i] == '1':
            ans += 1

        if i % 2 == 1 and s[i] == '0':
            ans += 1

    return min(ans, n - ans)


for _ in range(int(input())):
    n = int(input())
    s = input()
    n = len(s)

    print(solve(s, n))
