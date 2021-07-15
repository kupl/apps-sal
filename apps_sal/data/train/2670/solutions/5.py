def look_and_say_and_sum(n):
    from itertools import groupby
    e = '1'
    for i in range(n - 1):
        e = ''.join(str(list(b).count(a)) + a for a, b in groupby(e))
    return sum(map(int, e))
