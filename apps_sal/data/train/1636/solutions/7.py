max_n = 12000
max_factors = 1000000000
factors = [max_factors] * (max_n + 2)


def prod_sum(prod, sump, variant):
    factors[prod - sump] = min(factors[prod - sump], prod)
    for i in range(variant, max_n + 2):
        np = prod * i
        ns = sump + i - 1
        if np - ns > max_n:
            break
        prod_sum(np, ns, i)


prod_sum(1, 0, 2)


def productsum(n):
    return sum(list(set(factors[2:n+1])))

