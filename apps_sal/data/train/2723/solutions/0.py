N = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def average_string(s):
    try:
        return N[sum((N.index(w) for w in s.split())) // len(s.split())]
    except (ZeroDivisionError, ValueError):
        return 'n/a'
