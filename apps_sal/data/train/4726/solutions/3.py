def solve(s):
    M = 10 ** 9 + 7
    base = ord('Z') - ord('A') + 1
    num_cs = map(lambda c: 90 - ord(c), [c for c in s])
    acc = (0, 0)  # ( left-upside, total upside ) for the already traversed part of the list
    for num_c in num_cs:
        (ups_left, ups_tot) = acc
        ups_left_ = (ups_left * base + num_c) % M
        ups_tot_ = ((ups_left + 1) * num_c + ups_tot) % M
        acc = (ups_left_, ups_tot_)
    return acc[1]
