t = int(input())
mod = 1000000007


def get_sum(a, b, digits):
    sum = ((b + a) * (b - a + 1)) // 2
    return sum * digits


for _ in range(t):
    l, r = [int(x) for x in input().split()]
    l_digits = len(str(l))
    r_digits = len(str(r))
    ans = 0
    if(l_digits == r_digits):
        ans = get_sum(l, r, l_digits)
    else:
        ans += get_sum(l, ((10 ** l_digits) - 1), l_digits)
        ans += get_sum((10 ** (r_digits - 1)), r, r_digits)
        for i in range(l_digits + 1, r_digits):
            ans += get_sum(10 ** (i - 1), (10 ** i) - 1, i)

    print(ans % mod)
