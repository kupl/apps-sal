
import decimal
decimal.getcontext().prec = 16
decimal.getcontext().Emin = -1000000000
decimal.getcontext().Emax = 1000000000


def vowel(x):
    return x in 'aeiou'


def is_alice(s):
    if not vowel(s[0]) and not vowel(s[1]):
        return False

    for i in range(2, len(s)):
        if not vowel(s[i]) and (not vowel(s[i - 1]) or not vowel(s[i - 2])):
            return False

    return True


def fast_exp(x, p):
    x = decimal.Decimal(x)
    ans = decimal.Decimal(1)
    while p > 0:
        if p & 1:
            ans *= x
        x *= x
        p >>= 1
    return ans


def get_score(strings):
    k = len(strings)
    xc = [0] * 26
    fxc = [0] * 26

    for s in strings:
        f = [0] * 26
        for x in s:
            f[ord(x) - 97] += 1

        for i in range(26):
            if f[i] > 0:
                xc[i] += 1
                fxc[i] += f[i]

    pxc, pfxc = 1, 1
    for i in range(26):
        if xc[i] > 0:
            pxc *= xc[i]
            pfxc *= fxc[i]

    return decimal.Decimal(pxc) / fast_exp(pfxc, k)


for _ in range(int(input())):
    alice, bob = [], []
    for _ in range(int(input())):
        inp = input()
        if is_alice(inp):
            alice.append(inp)
        else:
            bob.append(inp)

    alice_score = get_score(alice)
    bob_score = get_score(bob)

    ratio = alice_score / bob_score
    if ratio > 10000000.0:
        print('Infinity')
    else:
        print(ratio)
