from collections import Counter


def merge_arrays(a, b):
    li = set()
    (c1, c2) = (Counter(a), Counter(b))
    for i in set(a + b):
        if i in c1 and i in c2:
            if c1[i] == c2[i]:
                li.add(i)
        else:
            li.add(i)
    return sorted(li)
