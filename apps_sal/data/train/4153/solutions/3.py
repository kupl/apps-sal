all_sums = {}


def helper():
    all_sums[0] = 0
    (rec, suma) = (0, 0)
    made = {0}
    for i in range(1, 2500000):
        cur = rec - i
        if cur < 0 or cur in made:
            cur = rec + i
        suma += cur
        made.add(cur)
        rec = cur
        all_sums[i] = suma
    return True


def rec(x):
    if not all_sums:
        helper()
    return all_sums[x - 1] if x >= 1 else 0
