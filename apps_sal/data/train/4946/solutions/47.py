from itertools import takewhile

house_numbers_sum = lambda lst: sum(takewhile(lambda n: n != 0, lst))
