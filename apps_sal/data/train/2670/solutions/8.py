from itertools import groupby
def look_and_say_and_sum(n):
    s='1'
    for _ in range(n-1):
        s=''.join(k+str(len(list(v))) for k,v in groupby(s))
    return sum(int(d) for d in s)
