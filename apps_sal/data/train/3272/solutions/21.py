from typing import List, Union

def find_average(nums: List[int]) -> Union[int, float]:
    """ Get the mean (average) of a list of numbers in an array. """
    return sum(nums) / len(nums) if nums else 0
