def max_tri_sum(numbers):

    a = []

    z = set(numbers)

    v = list(z)

    v.sort(reverse=True)

    b = v[0:3]

    s = sum(b)

    return s
