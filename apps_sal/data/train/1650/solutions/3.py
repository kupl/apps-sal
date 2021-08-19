def next_contig_number(n):
    n = [int(x) for x in str(n + 1)]
    for i in range(1, len(n)):
        n[i] = max(n[i], n[i - 1])
    return int(''.join(map(str, n)))


def find_all(sum_dig, digs):
    count = 0
    smallest = float('Inf')
    largest = float('-Inf')
    n = 10 ** (digs - 1)
    limit = 10 ** digs - 1
    while n < limit:
        n = next_contig_number(n)
        total = 0
        for x in map(int, str(n)):
            total += x
            if total > sum_dig:
                break
        if total == sum_dig:
            count += 1
            smallest = min(smallest, n)
            largest = max(largest, n)
    return [count, smallest, largest] if count else []
