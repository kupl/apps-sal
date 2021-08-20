def solve(n, k):
    s = str(n)
    for _ in range(k):
        i = next((i for i in range(len(s)) if i == len(s) - 1 or s[i] > s[i + 1]))
        s = s[:i] + s[i + 1:]
    return s
