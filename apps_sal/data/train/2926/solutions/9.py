from itertools import islice

def reverse(a):
    it = iter(''.join(x[::-1] for x in reversed(a)))
    return [''.join(islice(it, len(x))) for x in a]
