import re


def pseudo_sort(st):
    st, upper, lower = re.sub(r'[^ \w]', '', st).split(), [], []

    for i in st:
        if i[0].islower():
            lower.append(i)
        else:
            upper.append(i)

    return ' '.join(sorted(lower) + sorted(upper)[::-1])
