MOD = 1000000007


def main():
    s = input()
    n = len(s)

    ans = 0
    a_ct = 0
    p = 1
    for c in s:
        if c == 'a':
            a_ct += 1
            p *= 2
            p %= MOD
        else:
            ans += p
            ans %= MOD

    ans -= (n - a_ct)
    if ans < 0:
        ans += MOD
    ans %= MOD
    print(ans)


main()
