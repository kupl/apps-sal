import itertools
import operator


def product_sans_n(l):
    r = []
    p = list(itertools.accumulate(l, operator.mul))[-1]
    for i in range(len(l)):
        try:
            r.append(p // l[i])
        except:
            s = 1
            for j in range(len(l)):
                if i != j:
                    s *= l[j]
            r.append(s)
    return r
