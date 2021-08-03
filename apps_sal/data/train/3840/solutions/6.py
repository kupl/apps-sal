from bisect import bisect
MAX = 10 ** 7
counter = [0] * MAX
for base in range(2, int(MAX ** .5) + 1):
    prod = base ** 2
    while prod < MAX:
        counter[prod] += 1
        prod *= base

powers, frequencies = [0, 1], [-1, -1]
for power, frequency in enumerate(counter):
    if frequency:
        powers.append(power)
        frequencies.append(frequency)


def largest_power(n):
    idx = bisect(powers, n - 1) - 1
    return powers[idx], frequencies[idx]
