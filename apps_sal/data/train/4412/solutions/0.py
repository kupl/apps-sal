def subsets(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in subsets(collection[1:]):
        yield [first] + smaller
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [first + subset]  + smaller[n+1:]

def bucket_digit_distributions_total_sum(n):
    return sum(sum(map(int, sub)) for sub in subsets(str(n))) - n

def find(n, z):
    f_nf = bucket_digit_distributions_total_sum(n) + z
    while 1:
        n += 1
        if bucket_digit_distributions_total_sum(n) > f_nf:
            return n
