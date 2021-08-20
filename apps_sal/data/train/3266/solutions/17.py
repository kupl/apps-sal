from typing import Union


def my_first_kata(a: Union[int, str], b: Union[int, str]) -> Union[bool, int]:
    """
    Get a value based on types passed as the arguments:
      - `False` if either a or b (or both) are not numbers
      - `a % b + b % a` if both arguments are numbers
    """
    return False if not all(map(lambda _: type(_) in (int, float), [a, b])) else a % b + b % a
