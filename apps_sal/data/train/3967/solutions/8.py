from functools import lru_cache


@lru_cache(maxsize=None)
def f_checker(num):
    if all([i in ['3', '5', '8'] for i in str(num)]):
        count_8 = str(num).count('8')
        count_5 = str(num).count('5')
        count_3 = str(num).count('3')
        if count_8 >= count_5 and count_5 >= count_3:
            return num


def solve(a, b):
    counter = 0
    for num in range(a, b):
        res = f_checker(num)
        if res:
            counter += 1
    return counter
