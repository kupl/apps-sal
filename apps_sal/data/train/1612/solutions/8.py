def partition(n):
    return [[int(n / x)] for x in range(1, 1 + int(n / 2)) if n % x == 0]


def prod(a):
    prod = 1
    for n in a:
        prod *= n
    return prod


def score(a):
    return sum((n ** a.count(n) for n in reversed(sorted(set(a))))) * len(a)


def find_spec_prod_part(n, com):
    there_are_new = True
    partitions = partition(n)
    while there_are_new:
        there_are_new = False
        new_partitions = []
        for p in partitions:
            product = prod(p)
            if product < n:
                for new in partition(n / product):
                    if new[0] <= p[-1] and prod(p + new) <= n:
                        there_are_new = True
                        new_partitions.append(p + new)
            else:
                new_partitions.append(p)
        partitions = new_partitions
    if len(partitions) <= 1:
        return 'It is a prime number'
    result = None
    result_score = None
    for p in partitions:
        if len(p) > 1:
            s = score(p)
            if com == 'max' and (not result_score or result_score < s) or (com == 'min' and (not result_score or result_score > s)):
                result = p
                result_score = s
    return [result, result_score]
