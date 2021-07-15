from itertools import starmap
from operator import add

def split_and_add(numbers, n):
    for __ in range(n):
        mid, uneven = divmod(len(numbers), 2)
        numbers = list(starmap(add, zip([0] * uneven + numbers[:mid], numbers[mid:])))
    return numbers
