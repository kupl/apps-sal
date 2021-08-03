def multi(l_st):
    count = 1
    for x in l_st:
        count *= x
    return count


def add(l_st):
    count = 0
    for x in l_st:
        count += x
    return count


def reverse(string):
    return string[::-1]
