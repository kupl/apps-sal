from operator import itemgetter


def _collatz_len(n, lengths):
    if n in lengths:
        return [n, lengths[n]]
    count = 0
    curr_num = n
    nums = []
    while curr_num != 1:
        nums.append(curr_num)
        if curr_num in lengths:
            for (i, x) in enumerate(nums):
                if x not in lengths:
                    lengths[x] = count + lengths[curr_num] - i
            return [n, count + lengths[curr_num]]
        if curr_num % 2:
            nums.append(3 * curr_num + 1)
            curr_num = (3 * curr_num + 1) // 2
            count += 1
        else:
            curr_num //= 2
        count += 1
    count += 1
    for (i, x) in enumerate(nums):
        if x not in lengths:
            lengths[x] = count - i
    return [n, count]


def max_collatz_length(n):
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        return []
    curr_len = max_len = 0
    lengths = {1: 1, 2: 2}
    results = [_collatz_len(x, lengths) for x in range(1, n // 2 + 1)]
    for x in range(n // 2 + 1, n + 1):
        if x % 2:
            results.append(_collatz_len(x, lengths))
        else:
            results.append([x, results[x // 2 - 1][1] + 1])
    return max(results, key=itemgetter(1))
