from bisect import bisect
sum_dig = lambda n, D={str(d): d * d for d in range(10)}: sum(map(D.get, str(n)))
def is_happy(n): return n > 4 and is_happy(sum_dig(n)) or n == 1


happy_set = set(filter(is_happy, range(100)))
for n in range(100, 3 * 10 ** 5):
    if sum_dig(n) in happy_set:
        happy_set.add(n)


def performant_numbers(n, happy_list=sorted(happy_set)): return happy_list[:bisect(happy_list, n)]
