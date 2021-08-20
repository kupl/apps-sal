from itertools import count


def next_numb(val):
    if val >= 9999999999:
        return 'There is no possible number that fulfills those requirements'
    for i in count(val + 1):
        s = str(i)
        if i % 2 == 1 and i % 3 == 0 and (len(s) == len(set(s))):
            return i
