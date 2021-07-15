from collections import Counter


def repeat_sum(l):
    counter = sum((Counter(set(el)) for el in l), Counter())
    return sum(num for num in counter if counter[num] > 1)

