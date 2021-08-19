from bisect import bisect


def max_sumDig(n_max, max_sum):
    numbers = []
    for n in range(1000, n_max + 1):
        s = str(n)
        if all((sum(map(int, s[i:i + 4])) <= max_sum for i in range(len(s) - 3))):
            numbers.append(n)
    res_sum = sum(numbers)
    res_count = len(numbers)
    res_avg = 1.0 * res_sum / res_count
    idx = bisect(numbers, res_avg)
    (a, b) = numbers[idx - 1:idx + 1]
    closest = a if res_avg - a <= b - res_avg else b
    return [res_count, closest, res_sum]
