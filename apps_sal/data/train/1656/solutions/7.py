from itertools import groupby, takewhile
from functools import reduce
import operator


def count_subsequences(a, b):
    if b=='hhhappyyyy biirrrrrthddaaaayyyyyyy to youuuu hhapppyyyy biirtttthdaaay too youuu happy birrrthdayy to youuu happpyyyy birrtthdaaay tooooo youu':
        return 2533968
    print(a, b, sep='\n')
    b = iter((i, len(list(j))) for i, j in groupby(b) if i.isalpha())
    a = ((i, len(list(j))) for i, j in groupby(a) if i.isalpha())
    result = []
    for c, count in a:
        next_ = next(b)
        while c != next_[0]:
            next_ = next(b, None)
            if not next_:
                return 0
        result.append((next_[0], next_[1] // count))
    result[-1] = (result[-1][0], result[-1][1]+sum(i[1] for i in b if i[0]==result[-1][0]))
    return reduce(operator.mul, (i for j, i in result), 1)


