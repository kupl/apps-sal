
import itertools


def slogan_maker(a):
    a2 = list(set(a))
    a2.sort(key=a.index)
    x = []
    result = list(itertools.permutations(a2, len(a2)))
    for i in range(0, len(result)):
        x.append(join1(result[i]))
        i += 1
    return x


def join1(x):
    x1 = list(x)
    return ' '.join(x1)
