from math import gcd

base1 = {3: (121, 22, 4),
         4: (1331, 242, 44, 8),
         5: (14641, 2662, 484, 88, 16)}
base2 = {3: (111, 22, 3),
         4: (1111, 222, 33, 4),
         5: (11111, 2222, 333, 44, 5)}

memo = {100: 0}


def find_int_inrange(a, b):
    for n in range(max(memo) + 1, b + 1):
        base = 3 if n < 1000 else 4 if n < 10000 else 5
        digits = [int(d) for d in str(n)]
        score1 = sum(b * d for b, d in zip(base1[base], digits))
        score2 = sum(b * d for b, d in zip(base2[base], digits))
        hcf = gcd(score1, score2)
        common = 0
        for factor in range(2, hcf + 1):
            if score1 % factor == score2 % factor == 0:
                common += 1
        memo[n] = common
    maxCommon, numbers = 0, []
    for n in range(a, b + 1):
        m = memo[n]
        if maxCommon < m:
            maxCommon, numbers = m, [n]
        elif maxCommon == m:
            numbers.append(n)
    return [maxCommon] + numbers
