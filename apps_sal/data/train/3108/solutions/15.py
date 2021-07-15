def multi_table(number: int) -> str:
    """ Get multiplication table for number that is always an integer from 1 to 10. """
    return "\n".join([f"{_it} * {number} = {_it * number}" for _it in range(1, 11)])
