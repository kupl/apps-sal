from itertools import count

def four_piles(apples, y):
    for x in count(2 * y, y):
        plus = x + y
        minus = x - y
        star = x * y
        slash = x / y
        total = plus + minus + star + slash
        if total == apples:
            return [plus, minus, star, slash]
        if total > apples:
            return []
