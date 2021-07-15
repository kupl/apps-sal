from itertools import groupby

class Conseq:
    def __init__(self):
        self.value = None
        self.key = 0
    def __call__(self, value):
        if self.value is None or (value != self.value + 1):
            self.key += 1
        self.value = value
        return self.key

def serial(it):
    first = last = next(it)
    for last in it:
        pass
    if first == last:
        yield str(first)
    elif first + 1 == last:
        yield str(first)
        yield str(last)
    else:
        yield '{}-{}'.format(first, last)

def solution(args):
    return ','.join(r for _, grp in groupby(args, key=Conseq()) for r in serial(grp))
