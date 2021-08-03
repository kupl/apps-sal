import re


def sort_nested_list(arr):
    s = str(arr)
    ns = sorted(re.findall(r"\d+", s), key=int, reverse=True)
    return eval(re.sub(r"\d+", lambda _: ns.pop(), s))
