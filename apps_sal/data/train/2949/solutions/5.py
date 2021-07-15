from itertools import zip_longest

def split_and_add(numbers, n):
    while len(numbers) > 1 and n:
        n -= 1
        m = len(numbers) // 2
        it = zip_longest(reversed(numbers[:m]), reversed(numbers[m:]), fillvalue=0)
        numbers = list(map(sum, it))[::-1]
    return numbers
