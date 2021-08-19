from collections import defaultdict
import gc


def scramble(s1, s2):
    #   print(s1,s2)
    a = defaultdict(lambda: False)
    for item in s2:
        a[item] = a.get(item, 0) + 1
    # print(a)
    b = defaultdict(lambda: False)
    for item in s1:
        b[item] = b.get(item, 0) + 1
    # print(b)
    try:
        for item in a:
            #           print(a[item],b[item])
            if b[item] and a[item] <= int(b[item]):
                # print(item)
                pass
            else:
                return False
        return True
    finally:
        del a, b, s1, s2
        gc.collect()
