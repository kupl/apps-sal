def solve(n, s):
    def _doit(l, r, c):
        ch = chr(ord('a') + c)
        if l + 1 == r:
            return int(s[l] != ch)
        mid = l + (r - l) // 2
        non1 = sum(int(s[i] != ch) for i in range(l, mid))
        non2 = sum(int(s[i] != ch) for i in range(mid, r))
        return min(non1 + _doit(mid, r, c + 1), non2 + _doit(l, mid, c + 1))
    return _doit(0, n, 0)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
