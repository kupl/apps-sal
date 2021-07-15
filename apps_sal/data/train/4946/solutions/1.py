from itertools import takewhile; house_numbers_sum = lambda arr: sum(x for x in takewhile(lambda x: x!=0, arr))
