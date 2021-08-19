# precalculate results
results = {}
n, digits = 1, 0
while digits <= 1000:
    digits = len(str(sum(x**(n - x + 1) for x in range(1, n))))
    if digits not in results:
        results[digits] = n
    n += 1


def min_length_num(digits, max_num):
    n = results.get(digits, 0)
    return [True, n + 1] if n and n < max_num else [False, -1]
