MOD = 1000000007

def main():
    s = input()
    n = len(s)

    # each b contributes 1 flip to the first a before it, 2 flips to the second a before it, etc
    # in general, if there are k 'a's before a b, then add 2^(k + 1) - 1 flips
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

