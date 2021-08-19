def sflpf(n):
    i = 2
    first = True
    small = 0
    large = 0
    while i * i <= n:
        while n % i == 0:
            large = i
            if first:
                small = i
                first = False
            n /= i
        i += 1
    if small:
        return small + max(large, n)
    else:
        return 0


sflpf_of = [sflpf(i) for i in range(1, 2 * 10 ** 4)]


def sflpf_data(val, n):
    return [x for x in range(1, n + 1) if sflpf_of[x - 1] == val]
