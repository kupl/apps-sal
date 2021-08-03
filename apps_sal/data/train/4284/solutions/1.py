def array_leaders(numbers):
    res = []
    s = 0
    for n in reversed(numbers):
        if n > s:
            res.append(n)
        s += n
    res.reverse()
    return res


arrayLeaders = array_leaders
