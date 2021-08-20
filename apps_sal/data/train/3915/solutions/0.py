def solve(s):
    ans = []
    for ab in s.split('\n'):
        (carry, carried) = (0, 0)
        for (a, b) in zip(*map(lambda ss: map(int, ss[::-1]), ab.split())):
            carried += a + b
            carry += carried > 9
            carried //= 10
        ans.append(carry)
    return '\n'.join(('No carry operation' if not c else '%d carry operations' % c for c in ans))
