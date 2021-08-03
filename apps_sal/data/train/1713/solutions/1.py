
import sys


def count_calls(f, *args, **kwargs):
    total = 0

    def count(frame, event, arg):
        nonlocal total
        if event == 'call':
            total += 1
    sys.settrace(count)
    ret = f(*args, **kwargs)
    return total - 1, ret
