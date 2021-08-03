from collections import Counter


def work_on_strings(a, b):
    sa, sb = ("".join(x + x.upper() for x, y in Counter(s.lower()).items() if y % 2) for s in (a, b))
    return a.translate(str.maketrans(sb, sb.swapcase())) + b.translate(str.maketrans(sa, sa.swapcase()))
