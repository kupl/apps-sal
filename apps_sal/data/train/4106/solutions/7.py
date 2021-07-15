from itertools import count

def self_converge(p):
    width = len(str(p))
    previous = set()
    for i in count(1):
        s = sorted(str(p).ljust(width, '0'))
        n = int(''.join(reversed(s))) - int(''.join(s))
        if n is 0:
            return -1
        if n in previous:
            return i
        p = n
        previous.add(n)

