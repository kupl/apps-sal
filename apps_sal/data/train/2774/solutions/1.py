from itertools import cycle


def is_balanced(source, caps, i=0):
    it = iter(cycle([caps[i:i + 2] for i in range(0, len(caps), 2)]))
    cl = ''.join([e for e in source if e in caps])
    while i < len(source):
        if not cl:
            return True
        n = next(it)
        if n in cl:
            cl = cl.replace(n, '')
        i += 1
    return False
