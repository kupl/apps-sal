import re


def array(string):
    arr = re.split(',\\s*', string)
    if len(arr) < 3:
        return None
    return ' '.join(arr[1:-1])
