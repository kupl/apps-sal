def dSum(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans


def solve(n, d, step, ans):
    if n < 10:
        ans[n] = min(ans[n], step)
    left = dSum(n)
    right = n + d
    if step > 13:
        return step
    solve(left, d, step + 1, ans)
    solve(right, d, step + 1, ans)


for T in range(int(input())):
    (N, D) = [int(x) for x in input().split()]
    ans = {}
    for i in range(10):
        ans[i] = 100
    solve(N, D, 0, ans)
    (x, y) = [100, 100]
    for (i, j) in ans.items():
        if j != 100:
            x = i
            y = j
            break
    print(x, y)
