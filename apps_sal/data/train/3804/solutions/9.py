def min_length_num(num_dig, ord_max):
    result = results.get(num_dig, 0)
    return [True, result + 1] if result and result < ord_max else [False, -1]


results = {}
n = 1
digit = 0
while digit < 1000:
    digit = len(str(sum((x ** (n - x + 1) for x in range(1, n)))))
    if digit not in results:
        results[digit] = n
    n += 1
