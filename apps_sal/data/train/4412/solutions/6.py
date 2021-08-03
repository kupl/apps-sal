def find(n, z):

    lim = bucket_digit_distributions_total_sum(n) + z
    num = n

    while True:
        num += 1
        res = bucket_digit_distributions_total_sum(num)
        if lim < res:
            return num

    return num


def bucket_digit_distributions_total_sum(n):
    parts = get_partitions(list(str(n)), len(str(n)))
    buckets_sum = 0

    for p in parts:
        if len(p) > 1:
            b = [int(''.join(l)) for l in p]
            buckets_sum += sum(b)

    return buckets_sum


def get_partitions(lst, n):
    if n <= 0:
        yield []
        return
    else:
        curr = lst[n - 1]
        for part in get_partitions(lst, n - 1):
            for l in list(part):
                l.append(curr)
                yield part
                l.pop()
            yield part + [[curr]]


print(find(9457, 4))
