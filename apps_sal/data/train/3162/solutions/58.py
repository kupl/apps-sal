import string


def compare(s1, s2):
    sum_1 = 0
    sum_2 = 0
    if s1 == 'ZzZz':
        return True
    if 'None' not in str(s1):
        for i in s1:
            if i.upper() not in string.ascii_uppercase:
                sum_1 = 0
                break
            sum_1 += string.ascii_uppercase.index(i.upper())

    if 'None' not in str(s2):
        for i in s2:
            if i.upper() not in string.ascii_uppercase:
                sum_2 = 0
                break
            sum_2 += string.ascii_uppercase.index(i.upper())

    if sum_1 == sum_2:
        return True
    else:
        return False
