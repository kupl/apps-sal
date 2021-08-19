from itertools import count

# It's not worth it to memoize they numbers we reversed because a number is not always followed by its reversed in the result
# So we would have to save they numbers and return the minimum saved each time we find a new one
# All the numbers in this list are divisible by 9 so we can skip 88.9% of the possibilities


def gen():
    for x in count(0, 9):
        y = int(str(x)[::-1])
        if x != y and x % 10 and (x + y) % abs(x - y) == 0:
            yield x


numbers, result = gen(), []


def sum_dif_rev(n):
    while len(result) < n:
        result.append(next(numbers))
    return result[n - 1]
