from itertools import count

def is_keith_number(n):
    lst = list(map(int,str(n)))
    s   = sum(lst)
    for i in count(1):
        if s>=n: return n>9 and s==n and i
        lst, s = lst[1:] + [s], s*2-lst[0]
