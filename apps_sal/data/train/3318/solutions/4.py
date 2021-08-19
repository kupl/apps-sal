from itertools import zip_longest


def number_of_carries(a, b):
    (carry, li) = ([0], [])
    for (i, j) in zip_longest(str(a)[::-1], str(b)[::-1], fillvalue='0'):
        s = int(i) + int(j) + carry[-1]
        li.append(s % 10)
        if s > 9:
            carry.append(int(str(s)[0]))
            continue
        carry.append(0)
    return carry.count(1)
