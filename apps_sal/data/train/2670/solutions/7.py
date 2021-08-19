from itertools import groupby
d = ['1']


def look_and_say_and_sum(n):
    i = len(d) - 1
    s = d[i]
    for _ in range(i, n):
        x = ''
        for (c, g) in groupby(s):
            x += f'{len(list(g))}{c}'
        s = x
        d.append(s)
    return sum(map(int, d[n - 1]))


for i in range(1, 10):
    print(i, look_and_say_and_sum(i))
