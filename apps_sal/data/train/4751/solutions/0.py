def deficiently_abundant_amicable_numbers(a, b):
    c, d = list(map(sumOfDivs, (a, b)))
    return f'{ kind(a,c)} { kind(b,d) } { "not "*(a!=d or b!=c or a==b) }amicable'


def kind(n, sD): return 'abundant' if sD > n else 'perfect' if sD == n else 'deficient'
def sumOfDivs(n): return sum(d for d in range(1, int(n / 2 + 1)) if not n % d)
