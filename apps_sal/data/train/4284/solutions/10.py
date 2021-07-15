from itertools import accumulate

def array_leaders(numbers):
    if numbers[-1]: numbers.append(0)
    return [numbers[-i] for i,x in enumerate(accumulate(numbers[:0:-1]), 2) if numbers[-i] > x][::-1]
