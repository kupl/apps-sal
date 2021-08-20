m = 10 ** 9 + 7


def get_sum(a, b, digits):
    sum = (b + a) * (b - a + 1) // 2
    return sum * digits


for _ in range(int(input())):
    (l, r) = map(int, input().split())
    l_digits = len(str(l))
    r_digits = len(str(r))
    if l_digits == r_digits:
        ans = get_sum(l, r, l_digits)
    else:
        ans = get_sum(l, 10 ** l_digits - 1, l_digits) + get_sum(10 ** (r_digits - 1), r, r_digits)
        for i in range(l_digits + 1, r_digits):
            ans += get_sum(10 ** (i - 1), 10 ** i - 1, i)
    print(ans % m)
