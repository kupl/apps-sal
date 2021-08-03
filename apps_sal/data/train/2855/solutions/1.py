def dig_sum(n):
    return sum(map(int, str(n)))


terms = []
for b in range(2, 400):
    for p in range(2, 50):
        if dig_sum(b ** p) == b:
            terms.append(b ** p)
terms.sort()


def power_sumDigTerm(n):
    return terms[n - 1]
