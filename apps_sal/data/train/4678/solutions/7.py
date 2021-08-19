from collections import Counter


def find_the_missing_tree(trees):
    a = Counter(trees)
    a = str(a)
    # create list of counter
    a_s = (a.split())
    l_a = len(a_s)
    dd_a = str(a_s[l_a - 2])
    res_str = dd_a.translate({ord(i): None for i in ':'})
    res_int = int(res_str)
    return res_int
