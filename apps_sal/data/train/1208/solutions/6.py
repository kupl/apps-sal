m = 1000000007


def jk(n):
    arr = [1]
    cnt = 1
    ans = []
    for i in range(1, n + 1):
        cnt = (cnt * i) % m
        ans.append(cnt)
    for i in range(1, len(ans)):
        arr.append((arr[-1] * ans[i]) % m)
    return arr


t = jk(10**6)
for _ in range(int(input())):
    n = int(input())
    print(t[n - 1])
