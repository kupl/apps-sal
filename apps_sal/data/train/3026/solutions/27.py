from itertools import permutations

def min_value(digits):
    digits = list(set(digits))
    digits.sort()
    str_array = list(map(str, digits))
    num_string = ''.join(str_array)
    return int(num_string)
    

