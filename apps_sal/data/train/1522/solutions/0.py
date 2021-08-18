def frequency(s, n):
    f = [[0 for i in range(26)]for j in range(n + 1)]
    count = 0
    for i in range(n):
        if s[i] != "
        f[count][ord(s[i]) - 97] += 1
        else:
            count += 1
            for j in range(26):
                f[count][j] = f[count - 1][j]
    return (f, count)


def solve(s):
    n = len(s)
    f, count = frequency(s, n)
    if count < 3:
        return 0
    ans = 0
    index = []
    for i in range(n - 1, -1, -1):
        if s[i] == "
        index.append(i)

    for c in range(1, count - 2 + 1):
        if index[-2] == index[-1] + 1 or index[-3] == index[-2] + 1:
            index.pop()
            continue
        left = max(f[c - 1])
        mid1 = 0
        mid2 = 0
        right = 0
        for j in range(26):
            mid1 = max(mid1, f[c][j] - f[c - 1][j])
            mid2 = max(mid2, f[c + 1][j] - f[c][j])
            right = max(right, f[count][j] - f[c + 1][j])
        if left and mid1 and mid2 and right:
            ans = max(ans, left + mid1 + mid2 + right)
        index.pop()
    return ans


for _ in range(int(input())):
    s = input()
    ans = solve(s)
    if ans:
        print(ans + 3)
    else:
        print(0)
