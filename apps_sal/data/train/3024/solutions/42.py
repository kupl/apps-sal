from typing import List

def friend(array: List[str]) -> List[str]:
    """
    Filter a list of strings and return a list with only your friends name in it.
    Rule: If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
    """
    return list(filter(lambda name: len(name) == 4, array))
