import re


def sort_nested_list(arr):
    s = str(arr)
    ns = sorted(re.findall('\\d+', s), key=int, reverse=True)
    return eval(re.sub('\\d+', lambda _: ns.pop(), s))
