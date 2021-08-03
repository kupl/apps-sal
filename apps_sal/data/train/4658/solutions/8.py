def max_product(lst, l):
    st = sorted(lst)
    res = st[-l:]
    const = 1
    for i in res:
        const = const * i
    return const
