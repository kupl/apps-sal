def count_pal(n):  # amount of digits
    res = '1' + ('0' * n)
    temp = '9'
    l = []
    for x in range(1, len(res[1:])+1, 2):
        q = res[x:x+2]
        for _ in q:
            l.append(temp)
        temp += '0'
    return [int(l[-1]), sum(int(x) for x in l)]
