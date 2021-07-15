from typing import Union

def problem(a: Union[int, str]) -> Union[int, str]:
    """ Get the value multiplied by 50 and increased by 6. """
    try:
        return (a * 50) + 6
    except TypeError:
        return "Error"
