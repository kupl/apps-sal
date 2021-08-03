from itertools import count, islice, chain
import time


def mian_chowla():
    mc = [1]
    yield mc[-1]
    psums = set([2])
    newsums = set([])
    for trial in count(2):
        for n in chain(mc, [trial]):
            sum = n + trial
            if sum in psums:
                newsums.clear()
                break
            newsums.add(sum)
        else:
            psums |= newsums
            newsums.clear()
            mc.append(trial)
            yield trial


def pretty(s, f):
    arr = []
    for n in (islice(mian_chowla(), s, f)):
        arr.append(int(n))
    return arr


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        lst = pretty(0, n)
        sum = 0
        for i in range(n):
            print(lst[i], end=" ")
            sum += lst[i]
        print()
        print(sum)


__starting_point()
