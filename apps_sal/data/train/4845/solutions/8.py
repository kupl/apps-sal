import re


def sort_nested_list(A):
    a = str(A)
    b, a = a, re.sub('\[|\]', '', a)
    B = str(sorted(eval('[' + a + ']')))
    b, nl = list(re.sub("\d+", "
    for i in range(len(b)):
        b[i]=nl.pop() if b[i] == '
    return eval(''.join(b))
