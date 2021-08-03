import sys


def next_item(xs, item):
    f = 0
    try:
        for i in xs:
            if f == 1:
                return i
            if i == item:
                f = 1
    except:
        pass
