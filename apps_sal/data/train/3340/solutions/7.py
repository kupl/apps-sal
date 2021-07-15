def sharkovsky(a, b):
    if a == b:
        return False
    if a == 1:
        return False
    if b == 1:
        return a > 1
    c = get_highest_power_of_two_divisible_by_number(a)
    d = get_highest_power_of_two_divisible_by_number(b)
    if c == d:
        a //= c
        b //= d
        if a != 1 and b == 1:
            return True
        elif a == 1:
            return False
        else:
            return a < b
    elif c < d:
        a //= c
        b //= d
        if a == 1 and b != 1:
            return False
        elif a == 1 and b == 1:
            return False
        else:
            return True
    else:
        a //= c
        b //= d
        if a != 1 and b == 1:
            return True
        elif a == 1 and b == 1:
            return True
        else:
            return False

def get_highest_power_of_two_divisible_by_number(number):
    twos = []
    while number % 2 == 0:
        twos.append(2)
        number //= 2
    result = 2 ** len(twos)
    return result

def is_power_of_two(number):
    twos = []
    while number % 2 == 0:
        twos.append(2)
        number //= 2
    twos = remove_duplicates(twos)
    return twos == [2]

def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
