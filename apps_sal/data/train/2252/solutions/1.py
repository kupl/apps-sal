def main():
    n = int(input())
    ans = 0
    d = {}
    for i in range(n):
        s = input()
        cur = 0
        for c in s:
            cur ^= (1 << (ord(c) - ord('a')))
        ans += d.get(cur, 0)
        for j in range(26):
            ans += d.get(cur ^ (1 << j), 0)
        t = d.get(cur, 0) + 1
        d[cur] = t
    print(ans)
    return

def __starting_point():
    main()
__starting_point()
