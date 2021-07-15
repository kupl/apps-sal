def find(n: int) -> int:
    """ Get the sum of all multiples of 3 and 5 limited to `n`. """
    return sum(filter(lambda num: any([not num % 3, not num % 5]), range(n + 1)))
