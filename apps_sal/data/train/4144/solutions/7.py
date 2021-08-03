def abundant(n):
    def gen_div(a): return set(sum([[a // i, i]for i in range(1, int(a**.5) + 1)if a % i == 0], []))
    r = []
    for i in range(n, 0, -1):
        div_sum = sum(gen_div(i))
        if div_sum - i > i:
            return [[i], [div_sum - i * 2]]
