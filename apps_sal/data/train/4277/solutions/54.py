from typing import List


def difference_in_ages(ages: List[int]):
    """ Get a tuple with a structure: (youngest age, oldest age, difference between the youngest and oldest age). """
    return (min(ages), max(ages), max(ages) - min(ages))
