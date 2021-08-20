def main():
    md = 998244353
    s = input()
    n = len(s)
    al = True
    an = 1
    for (c0, c1) in zip(s, s[1:]):
        if c0 == c1:
            an = 0
        else:
            al = False
        if an == 0 and (not al):
            break
    if al:
        print(1)
        return
    if n == 2:
        print(2)
        return
    if n == 3:
        if s[0] == s[-1]:
            print(7)
        elif s[0] == s[1] or s[1] == s[2]:
            print(6)
        else:
            print(3)
        return
    ord0 = ord('a')
    r = sum((ord(c) - ord0 for c in s)) % 3
    if n % 3 == 0:
        d = pow(2, n // 3 - 1, md)
        if r == 0:
            an -= d * 2
        else:
            an += d
    print((pow(3, n - 1, md) - pow(2, n - 1, md) + an) % md)


main()
