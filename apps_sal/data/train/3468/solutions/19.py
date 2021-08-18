from collections import defaultdict
import gc


def scramble(s1, s2):
    a = defaultdict(lambda: False)
    for item in s2:
        a[item] = a.get(item, 0) + 1
    b = defaultdict(lambda: False)
    for item in s1:
        b[item] = b.get(item, 0) + 1
    try:
        for item in a:
            if b[item] and a[item] <= int(b[item]):
                pass
            else:
                return False
        return True
    finally:
        del a, b, s1, s2
        gc.collect()
