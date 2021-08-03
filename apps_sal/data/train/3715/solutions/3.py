from itertools import combinations as c


def nth_chandos_number(n):
    comb, generate, i = [1], [], 1
    while len(generate) <= n:
        generate.extend(sorted([j for k in range(1, len(comb) + 1) for j in c(comb, k) if j[0] == i]))
        i += 1
        comb.insert(0, i)
    return sum(5 ** i for i in generate[n - 1])
