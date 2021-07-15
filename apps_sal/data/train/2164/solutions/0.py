import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split())) + [0]*500000
    ans_S = 0
    a[n] = a[0] + m
    s = [0]*600600
    for i in range(n):
        s[i] = a[i + 1] - a[i]
    s[n] = -1
    for i in range(n):
        s[2*n - i] = s[i]
    for i in range(2*n + 1, 3*n + 1):
        s[i] = s[i - n]
    l, r = 0, 0
    z = [0]*600600
    for i in range(1, 3*n + 1):
        if i < r:
            z[i] = z[i - l]
        while i + z[i] <= 3*n and (s[i + z[i]] == s[z[i]]):
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    ans = []
    for i in range(n + 1, 2*n + 1):
        if z[i] < n:
            continue
        ans_S += 1
        ans.append((a[0] + a[2*n - i + 1]) % m)
    ans.sort()
    print(ans_S)
    print(*ans)
    return

def __starting_point():
    main()
__starting_point()
